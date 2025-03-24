import datetime

from django.shortcuts import render
from .models import PESELForm


def index(request):
    if request.method == "POST":
        pesel_form = PESELForm(pesel=request.POST["pesel"])
        if is_valid_pesel(pesel_form.pesel):
            birth_date, gender = get_birth_date_and_gender(pesel_form.pesel)
            return render(
                request,
                "result.html",
                {"pesel": pesel_form.pesel, "is_valid": True, "birth_date": birth_date, "gender": gender},
            )
        else:
            return render(request, "result.html", {"pesel": pesel_form.pesel, "is_valid": False})
    return render(request, "index.html")


def is_valid_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return False

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_digit = int(pesel[-1])

    checksum = sum(int(digit) * weight for digit, weight in zip(pesel[:-1], weights)) % 10
    checksum = 10 - checksum if checksum != 0 else 0

    return checksum == control_digit


def get_birth_date_and_gender(pesel):
    if not is_valid_pesel(pesel):
        raise ValueError("Invalid PESEL number.")

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if 80 < month < 93:
        year += 1800
    elif 0 < month < 13:
        year += 1900
    elif 20 < month < 33:
        year += 2000
    elif 40 < month < 53:
        year += 2100

    birth_date = datetime.date(year, month % 20, day)

    gender = "Kobieta" if int(pesel[-2]) % 2 == 0 else "Mężczyzna"

    return birth_date, gender
