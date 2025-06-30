# 🧠 SynForge — Synthetic Data Generator (CSV → AI-Ready)

**SynForge** is a free, open-source tool that turns your real-world tabular data into anonymized, GPT/CTGAN-generated synthetic datasets — enabling safe AI training, data sharing, and privacy compliance.

---

## ⚡️ Features

- Upload CSV or JSON files, or run from CLI  
- Automatically detect and anonymize personally identifiable information (PII)  
- Generate synthetic data that mimics structure and patterns of your real dataset  
- Export safe, synthetic versions of your datasets  
- Support domain-specific packs: Healthcare, Finance, Legal (coming soon)  
- Easy-to-use CLI and future API interfaces  

---

## 🛠 Example CLI Usage

```bash
synforge upload --file patient_data.csv --domain healthcare
synforge generate --model ctgan --rows 5000
synforge export --out ./synthetic_output.csv

## 🧱 Tech Stack

- Python 3.10+  
- `sdv` and `ctgan` for synthetic data generation  
- `faker` for anonymization  
- `Typer` for CLI interface  
- Planned: `FastAPI` for REST API version  
- Optional: Hugging Face Transformers integration  

---

## 🧩 Roadmap

| Milestone             | Status              |
|-----------------------|---------------------|
| Data Loader           | ✅ Completed        |
| Schema & Anonymizer   | 🚧 In Progress      |
| Synthetic Generator   | 🔜 Upcoming         |
| CLI Interface         | ✅ Working Prototype|
| API Interface         | 🔜 Planned          |
| Domain-specific Packs | 🔜 Planned          |

---

## 🤝 Contributing

We welcome contributors passionate about open-source, privacy, and AI!

1. Fork the repo  
2. Check open issues  
3. Submit a pull request  
4. Join discussions or contact us at **synforge@protonmail.com**

---

## 📄 License

MIT License. Free for personal and commercial use.

---

> SynForge is committed to enabling privacy-safe, accessible AI data generation — join us to build the future of synthetic data!

