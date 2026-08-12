from django.shortcuts import render

from .forms import DivideMultiplyForm
from .logic import compute


def calculator_view(request):
    result = None

    if request.method == "POST":
        form = DivideMultiplyForm(request.POST)
        if form.is_valid():
            dividend = form.cleaned_data["dividend"]
            divisor = form.cleaned_data["divisor"]
            result = compute(dividend, divisor)
    else:
        form = DivideMultiplyForm()

    return render(request, "calculator/calculator.html", {
        "form": form,
        "result": result,
    })
