# Predict-Price-hotel-Machine-Learning

\documentclass[a4paper, 12pt]{book}
\usepackage{graphicx}
\usepackage[french]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{multirow}
\usepackage{listings}
\usepackage{float}
\usepackage{url}
\usepackage[french]{algorithm}
\usepackage{style/myalgorithm}
\usepackage{amsmath,amsfonts,amssymb}
\newcommand{\fBm}{\emph{fBm}~}
\newcommand{\etal}{\emph{et al.}~}
\newcommand{\glAd}{\emph{GL4D}~}
\newcommand{\apiopengl}{API OpenGL\textsuperscript{\textregistered}~}
\newcommand{\opengl}{OpenGL\textsuperscript{\textregistered}~}
\newcommand{\opengles}{OpenGL\textsuperscript{\textregistered}ES~}
\newcommand{\clang}{langage \texttt{C}}
\newcommand{\codesource}{\textsc{Code source}~}
\usepackage{textcomp}
\usepackage{siunitx}
\floatstyle{ruled}
\newfloat{programslist}{htbp}{locs}
\newcommand{\listofprograms}{\listof{programslist}{Liste des codes source}}
\newcounter{program}[subsection]
\renewcommand{\theprogram}{\arabic{chapter}.\arabic{program}}

\newenvironment{program}[1]{
  \if\relax\detokenize{#1}\relax
  \gdef\mycaption{\relax}
  \else
  \gdef\mycaption{#1}
  \fi
  \refstepcounter{program}
  \addcontentsline{locs}{section}{#1}
  \footnotesize
}{
  \begin{description}
    % \item[\codesource \theprogram]--~\mycaption
  \end{description}
}

\begin{document}
\begin{titlepage}
  \begin{center}
    \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
      \includegraphics[height=2.0cm]{images/m1info.png}~&~
      \includegraphics[height=2.5cm]{images/logop__.jpg}
    \end{tabular*}
    \small 
    \rule{\textwidth}{.5pt}~\\
    \large 
    \textsc{Université Paris 8 - Vincennes à Saint-Denis}\vspace{0.5cm}\\
    \textbf{Master Informatique des Systèmes Embarqués}\vspace{4.0cm}\\
    \Large
    \textbf{Big-Data}\vspace{.1cm}\\
    \Large
    \textbf{Predict-Price-hotel-Machine-Learning}\vspace{.5cm}\\
    \large
    \textbf{Aimen \textsc{GANA}}\vspace{0.5cm}\\
    \large
    \textbf{Hammou \textsc{SABBAR}}\vspace{6.5cm}\\
    \large
    \textbf {Université Paris VIII : Rakia \textsc{JAZIRI}}\vspace{.5cm}\\
    Date de rendu : le 06/01/2019\vspace{1.75cm}\\
  \end{center}\vspace{1.5cm}~\\
  \begin{tabular}{ll}
    % \hspace{-0.45cm}Organisme d'accueil~:~&~XXXXXXX (si stage)\\
    % \hspace{-0.45cm}Tuteur -- Organisme d'accueil~:~&~Prénom \textsc{Nom} (si stage)\\

    
  \end{tabular}
\end{titlepage}
\frontmatter

\chapter*{Projet : Predict-Price-hotel-Machine-Learning }
Notre projet consiste a prédire la catégorie des prix des hôtels (cher, moyen, pas cher) en Île-de-France, à partir d’apprentissage de Machine Learning avec Sklearn,  Scikit-learn est une bibliothèque libre Python destinée à l'apprentissage automatique. Elle comprend notamment des fonctions pour estimer des forêts aléatoires, des régressions logistiques, des algorithmes de classification, et les machines à vecteurs de support. Nous ce qui va nous intéressé c’est les algorithmes de classification dans ce projet. \\
Elle est développée par de nombreux contributeurs notamment dans le monde académique par des instituts français d'enseignement supérieur et de recherche comme Inria et Télécom ParisTech. \\
Nous somme basé sur ces Statistique suivant : \\
\hspace*{2cm} - Les prix\\
\hspace*{2cm} - Les avis \\
\hspace*{2cm} - Nombre des étoiles d’hôtel \\ 

Nous avons récupéré les données sur le site Tripadvisor les noms des hôtels, localisation, les prix, les avis,servies proposer, dans un fichier csv, puis nous avons remarquer que les nom et les localisation pouvait pas être traité par machine laerning en format String, nous pouvons trouver une autre présentation sauf nous ne disposons pas d’un temps suffisant. 
Pour l’apprentissage nous basons sur 9 critères les prix, nombre d’étoile et les avis (Excellent, Très bon, Moyen, Médiocre, Horrible et le nombre des commentateur)\\

Nous avons utiliser l’algorithme KNN que nous avons  vue durant le cours pour faire la prédiction sur la classe des l’hôtels,  nous avons utilisé 80 \\
