// App.js (React / Next.js)
import React, { useState } from 'react';

export default function GPAHorizon() {
  const [subjects, setSubjects] = useState([{ name: '', grade: '', credits: '' }]);
  const [result, setResult] = useState(null);

  const addSubject = () => setSubjects([...subjects, { name: '', grade: '', credits: '' }]);

  const calculate = async () => {
    const response = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ system: 'KZ', subjects }),
    });
    const data = await response.json();
    setResult(data);
  };

  return (
    <div className="min-h-screen bg-slate-50 p-8 font-sans">
      <div className="max-w-2xl mx-auto bg-white rounded-2xl shadow-xl p-8">
        <h1 className="text-3xl font-bold text-indigo-600 mb-2">GPA Horizon</h1>
        <p className="text-slate-500 mb-8">Преврати свои оценки в стратегию поступления.</p>

        {subjects.map((s, i) => (
          <div key={i} className="flex gap-4 mb-4">
            <input placeholder="Предмет" className="border p-2 rounded w-full" 
              onChange={e => { subjects[i].name = e.target.value; setSubjects([...subjects]); }} />
            <input placeholder="Оценка" type="number" className="border p-2 rounded w-24" 
              onChange={e => { subjects[i].grade = Number(e.target.value); setSubjects([...subjects]); }} />
          </div>
        ))}

        <button onClick={addSubject} className="text-indigo-600 font-medium mb-6">+ Добавить предмет</button>
        <button onClick={calculate} className="w-full bg-indigo-600 text-white p-3 rounded-lg font-bold hover:bg-indigo-700">
          Сгенерировать Academic DNA
        </button>

        {result && (
          <div className="mt-8 p-6 bg-indigo-50 rounded-xl border border-indigo-100">
            <h2 className="text-xl font-bold text-indigo-900">Результат: {result.gpa} GPA</h2>
            <p className="mt-2"><strong>Ваш DNA:</strong> {result.academic_dna}</p>
            <p className="mt-2 text-slate-700">{result.recommendation}</p>
          </div>
        )}
      </div>
    </div>
  );
}
