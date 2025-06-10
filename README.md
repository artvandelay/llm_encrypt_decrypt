# LLM Text Compression Demo (ts_zip)

A Streamlit web application demonstrating text compression using Large Language Models, based on Fabrice Bellard's groundbreaking ts_zip utility.

## 🚀 Live Demo

**[Try the app here →](https://llmencryptdecrypt-euyfofcjh8bf2tutha2zox.streamlit.app/)**

## What is ts_zip?

ts_zip is a revolutionary text compression utility that achieves **superior compression ratios** compared to traditional compressors by leveraging Large Language Models. Instead of finding repetitive patterns, it uses an LLM to predict the probability of the next token, then encodes text based on these predictions using arithmetic coding.

## 🏆 Compression Performance

The compression ratio is measured in **bits per byte (bpb)** - lower is better:

| File | Original Size | xz (bpb) | **ts_zip (bpb)** | Improvement |
|------|---------------|----------|------------------|-------------|
| alice29.txt | 152,089 bytes | 2.551 | **1.142** | 2.2x better |
| book1 | 768,771 bytes | 2.717 | **1.431** | 1.9x better |
| enwik8 | 100,000,000 bytes | 1.989 | **1.106** | 1.8x better |
| enwik9 | 1,000,000,000 bytes | 1.707 | **1.084** | 1.6x better |
| linux-1.2.13.tar | 9,379,840 bytes | 1.441 | **1.021** | 1.4x better |

*Results show ts_zip consistently outperforms traditional compression across different text types.*

## 🔬 How It Works

1. **Language Model**: Uses RWKV 169M v4 model (quantized to 8-bit)
2. **Prediction**: Model predicts probabilities of next tokens
3. **Encoding**: Arithmetic coder encodes tokens based on probabilities
4. **Deterministic**: Results are reproducible across different hardware

## ⚠️ Important Considerations

- **GPU Required**: 4GB+ VRAM needed for reasonable performance
- **Speed**: Up to 1 MB/s on RTX 4090 (slower than traditional compressors)
- **Text Only**: Optimized for text files, especially English content
- **Experimental**: No backward compatibility guaranteed between versions

## 🛠️ Technical Details

- **Model**: RWKV 169M v4 (169 million parameters)
- **Quantization**: 8-bit parameters, BF16 evaluation
- **Training**: Primarily English text, supports other languages and code
- **Reproducibility**: Deterministic across different hardware configurations

## 🚢 Running Locally

### Using Docker
```bash
docker build -t ts-zip-demo .
docker run -p 8501:8501 ts-zip-demo
```

### Manual Installation
```bash
pip install -r requirements.txt
streamlit run app/main.py
```

## 📊 Benchmarks

For comprehensive benchmarks and comparisons with other compression algorithms, visit the [Large Text Compression Benchmark](http://mattmahoney.net/dc/text.html).

## 🙏 Attribution

This demo is based on the original ts_zip utility created by **Fabrice Bellard**.

- **Original Project**: [https://bellard.org/ts_zip/](https://bellard.org/ts_zip/)
- **Author**: Fabrice Bellard
- **Related**: See also [ts_sms](https://bellard.org/ts_sms/) for small message compression

## 📝 License

Please refer to the original ts_zip licensing terms. This demo is for educational and demonstration purposes.

## 🔗 Links

- [Original ts_zip by Fabrice Bellard](https://bellard.org/ts_zip/)
- [Large Text Compression Benchmark](http://mattmahoney.net/dc/text.html)
- [RWKV Language Model](https://github.com/BlinkDL/RWKV-LM)

---

*Experience the future of text compression - where AI meets data compression! 🤖📦*
