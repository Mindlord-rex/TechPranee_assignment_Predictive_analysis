\documentclass{article}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{hyperref}

\definecolor{codegreen}{rgb}{0,0.6,0}
\definecolor{codegray}{rgb}{0.5,0.5,0.5}
\definecolor{codepurple}{rgb}{0.58,0,0.82}

\lstdefinestyle{mystyle}{
    backgroundcolor=\color{white},   
    commentstyle=\color{codegreen},
    keywordstyle=\color{magenta},
    numberstyle=\tiny\color{codegray},
    stringstyle=\color{codepurple},
    basicstyle=\ttfamily\footnotesize,
    breakatwhitespace=false,         
    breaklines=true,                 
    keepspaces=true,                 
    numbers=left,       
    numbersep=5pt,                  
    showspaces=false,                
    showstringspaces=false,
    showtabs=false,                  
    tabsize=2
}

\lstset{style=mystyle}

\title{Predictive Analysis API for Manufacturing Operations}
\author{Your Name}
\date{\today}

\begin{document}
\maketitle

\section{Overview}
A RESTful API built with FastAPI to predict machine downtime using manufacturing data. Supports data upload, model training, and predictions.

\tableofcontents

\section{Features}
\begin{itemize}
    \item Upload manufacturing data via CSV
    \item Train logistic regression model
    \item Predict downtime with confidence scores
    \item Persistent model storage using \texttt{joblib}
\end{itemize}

\section{Setup}
\subsection{Prerequisites}
\begin{itemize}
    \item Python 3.8+
    \item pip
\end{itemize}

\subsection{Installation}
\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}[language=bash]
git clone https://github.com/your-username/machine-downtime-api.git
cd machine-downtime-api
    \end{lstlisting}
    
    \item Install dependencies:
    \begin{lstlisting}[language=bash]
pip install -r requirements.txt
    \end{lstlisting}
\end{enumerate}

\subsection{Run the API}
\begin{lstlisting}[language=bash]
uvicorn main:app --reload
\end{lstlisting}
Access the API at \url{http://localhost:8000}

\section{API Endpoints}
\subsection{Upload Data (POST /upload)}
\textbf{Purpose}: Upload CSV dataset\\
\textbf{Request}:
\begin{lstlisting}[language=bash]
curl -X POST -F "file=@sample_data.csv" http://localhost:8000/upload
\end{lstlisting}
\textbf{Success Response}:
\begin{lstlisting}[language=json]
{ "message": "Data uploaded successfully" }
\end{lstlisting}

\subsection{Train Model (POST /train)}
\textbf{Purpose}: Train model on uploaded data\\
\textbf{Request}:
\begin{lstlisting}[language=bash]
curl -X POST http://localhost:8000/train
\end{lstlisting}
\textbf{Success Response}:
\begin{lstlisting}[language=json]
{ "accuracy": 0.92, "f1_score": 0.89 }
\end{lstlisting}

\subsection{Predict Downtime (POST /predict)}
\textbf{Purpose}: Predict machine downtime\\
\textbf{Request}:
\begin{lstlisting}[language=bash]
curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 80, "Run_time": 120}' http://localhost:8000/predict
\end{lstlisting}
\textbf{Success Response}:
\begin{lstlisting}[language=json]
{ "Downtime": "Yes", "Confidence": 0.85 }
\end{lstlisting}

\section{Dataset}
\textbf{Format}: CSV with columns \texttt{Machine\_ID}, \texttt{Temperature}, \texttt{Run\_time}, \texttt{Downtime\_Flag}\\
\textbf{Sample Data}:
\begin{lstlisting}[language=csv]
Machine_ID,Temperature,Run_time,Downtime_Flag
M0,72,150,0
M1,85,200,1
\end{lstlisting}

\section{Model Details}
\begin{itemize}
    \item \textbf{Algorithm}: Logistic Regression (\texttt{scikit-learn})
    \item \textbf{Input Features}: \texttt{Temperature}, \texttt{Run\_time}
    \item \textbf{Output}: Binary classification (0 = No Downtime, 1 = Downtime)
    \item \textbf{Persistence}: Saved to \texttt{trained\_model.pkl}
\end{itemize}

\end{document}
