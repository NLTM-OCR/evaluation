# Evaluation Measures for Bhaasha OCR

## Setup
- Using Python = 3.10+
- Install Dependencies `pip install -r requirements.txt`

## Usage

This module can be used to calculate CRR (Character Recognition Rate) and WRR (Word Recognition Rate)
for a pair of text.

### Example

```python
from process import evaluate
crr, wrr = evaluate("ब्राउन फॉक्स", "ब्रान फॉक्स", "hindi")
```

## Contact

You can contact **[Krishna Tulsyan](mailto:krishna.tulsyan@research.iiit.ac.in)** for any issues or feedbacks.

## References

**[JiWER](https://github.com/jitsi/jiwer)**