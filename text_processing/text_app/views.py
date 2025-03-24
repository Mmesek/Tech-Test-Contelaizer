from django.shortcuts import render, redirect


def index(request):
    if request.method == "POST":
        text = str(request.FILES["file"].read().decode())
        modified_text = "\n".join(
            " ".join(word[0] + "".join(reversed(word[1:-1])) + word[-1] for word in line.split(" ") if line)
            for line in text.splitlines()
        )
        print(modified_text)
        return render(request, "result.html", {"modified_text": modified_text})
    return render(request, "index.html")
