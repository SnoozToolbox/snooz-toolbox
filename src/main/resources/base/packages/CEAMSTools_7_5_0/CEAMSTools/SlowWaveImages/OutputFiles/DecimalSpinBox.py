from qtpy.QtWidgets import QDoubleSpinBox


class DecimalSpinBox(QDoubleSpinBox):
    """Accept either decimal separator while displaying values in the Qt locale."""

    def _localized_text(self, text: str) -> str:
        separator = self.locale().decimalPoint()
        return text.translate(str.maketrans({".": separator, ",": separator}))

    def validate(self, text: str, position: int):
        state, _, _ = super().validate(self._localized_text(text), position)
        return state, text, position

    def valueFromText(self, text: str) -> float:
        return super().valueFromText(self._localized_text(text))
