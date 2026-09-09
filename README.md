# 🎓 AI-Powered Student Performance Prediction System

A simple, beginner-friendly project that uses **Machine Learning** to predict
a student's final exam score based on 5 factors:

- Study hours per day
- Attendance percentage
- Previous exam score
- Sleep hours per day
- Assignments completed percentage

It has a clean web page where you type in a student's numbers and instantly
get a predicted score, plus a performance label (Excellent / Good / Needs
Improvement / At Risk).

---

## 🧠 How it works (explained simply)

Think of Machine Learning like teaching a student by showing worked examples:

1. **We show the model 500 example students** — for each one, we know their
   study hours, attendance, etc., AND their actual final score.
2. **The model finds the pattern.** We use a `Linear Regression` model —
   the simplest ML algorithm there is. It learns a "weight" (importance
   number) for each factor. For example, it might learn that each extra
   hour of studying is worth about +4 points.
3. **Prediction = simple math.** Once trained, predicting a new student's
   score is just:
   ```
   score = (weight1 × study_hours) + (weight2 × attendance) + ... + base_number
   ```
   No black-box magic — it's a weighted sum, which is why Linear Regression
   is great for beginners to understand.
4. **The website is the "frontend."** It's just a form. When you click
   "Predict," the numbers you typed are sent to the Python backend, run
   through the formula above, and the answer is shown back to you.

---

## 📁 Project structure

```
student_performance_project/
│
├── data/
│   ├── generate_data.py      # Creates a fake-but-realistic dataset
│   └── student_data.csv      # The generated dataset (500 students)
│
├── model/
│   ├── train_model.py        # Trains the ML model on the dataset
│   └── student_model.pkl     # The saved, trained model
│
├── templates/
│   └── index.html            # The web page (frontend)
│
├── static/
│   └── style.css             # Styling for the web page
│
├── app.py                    # Flask backend server
├── requirements.txt          # Python packages needed
└── README.md                 # This file
```

---

## ▶️ How to run it yourself

1. **Install the requirements** (only needed once):
   ```
   pip install -r requirements.txt
   ```

2. **(Optional) Regenerate the data and retrain the model.**
   A trained model is already included, but you can rebuild it:
   ```
   python data/generate_data.py
   python model/train_model.py
   ```

3. **Start the web app:**
   ```
   python app.py
   ```

4. **Open your browser** and go to:
   ```
   http://127.0.0.1:5000
   ```

5. Fill in the form and click **"Predict Performance"** to see the result!

---

## 🔍 Where's the "AI"?

The AI/ML part lives entirely in `model/train_model.py`. That's the only
place "learning" happens. Everything else (`app.py`, the HTML, the CSS) is
just plumbing to let a human interact with that trained model through a
web page instead of the command line.

---

## 🚀 Ideas to extend this project (great for a class presentation)

- Swap `LinearRegression` for `RandomForestRegressor` and compare accuracy.
- Add more features, e.g. "hours on social media" or "part-time job hours."
- Turn it into a **classification** problem instead: predict Pass/Fail
  instead of an exact score (use `LogisticRegression`).
- Add a chart (e.g. with Chart.js) showing which factor mattered most.
- Replace the synthetic dataset with a real one (there are public "student
  performance" datasets on Kaggle) for a more authentic demo.
- Deploy it online with a free host like Render or PythonAnywhere so
  others can try it without installing anything.

---

## ⚠️ Note on the data

The dataset used here is **synthetically generated** (fake, created by a
formula + randomness) so the project runs immediately without needing to
download anything. It behaves realistically (more study hours → higher
scores) but does **not** represent real students.
