# 📚 Imuta
### Learn smarter. Grow further.

Imuta is a Python-based study management application designed to help students organise their subjects, track learning topics and monitor their academic progress.

## 🎯 Project Goals

Imuta aims to help students:
- Organise academic subjects.
- Add and manage individual learning topics.
- Track completed and remaining topics.
- Monitor learning progress.
- Plan study sessions.
- Understand their academic progress through analytics.

## 🛠️ Technologies

- **Python** – Core application logic.
- **Streamlit** – User interface and dashboard.
- **Pandas** – Data management and analysis.
- **Matplotlib** – Data visualisation.
- **SQLite** – Planned persistent data storage.

## 📂 Project Structure

```text
Imuta/
├── app.py
├── core/
│   └── study_manager.py
├── database/
│   ├── db.py
│   └── schema.sql
├── models/
│   ├── subject.py
│   └── topic.py
├── pages/
│   ├── dashboard.py
│   ├── subjects.py
│   ├── planner.py
│   ├── sessions.py
│   └── analytics.py
└── requirements.txt
```

## 🚀 Running Imuta Locally

1. Clone the repository:

```bash
git clone https://github.com/me729-cpk/Imuta.git
```

2. Enter the project directory:

```bash
cd Imuta
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
python -m streamlit run app.py
```

## 🌐 Live Demo

[Open Imuta](https://imuta-study.streamlit.app/)

## 📈 Current Development Status

Imuta is actively being developed.

Completed foundations:
- Initial Streamlit dashboard.
- Subject and Topic classes.
- Topic completion tracking.
- Subject progress calculations.
- Modular project organisation.
- StudyManager foundation.

Planned improvements:
- Connect the core Python logic to the interface.
- Implement persistent data storage.
- Develop functional study planning and analytics.
- Improve personalised study recommendations.

## 👨‍💻 Developer

Created by **me729-cpk** as a learning and software development project.

