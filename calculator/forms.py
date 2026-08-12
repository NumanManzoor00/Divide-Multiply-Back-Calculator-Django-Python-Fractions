from django import forms


class DivideMultiplyForm(forms.Form):
    dividend = forms.DecimalField(
        label="Number to divide",
        max_digits=30,
        decimal_places=10,
        widget=forms.NumberInput(attrs={
            "step": "any",
            "placeholder": "e.g. 100",
            "class": "input",
        }),
    )
    divisor = forms.DecimalField(
        label="Divide / multiply by",
        max_digits=30,
        decimal_places=10,
        widget=forms.NumberInput(attrs={
            "step": "any",
            "placeholder": "e.g. 3",
            "class": "input",
        }),
    )

    def clean_divisor(self):
        divisor = self.cleaned_data["divisor"]
        if divisor == 0:
            raise forms.ValidationError("Cannot divide by zero.")
        return divisor
