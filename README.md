mkpdf
====

png/jpg/gif/bmpの.bbを自動生成しつつ.texを.pdfを生成します．

## Usage

    python mkpdf.py document.tex

## Sample

.tex 内に以下の記述がある場合

    \begin{figure}
      \centering
      \includegraphics[width=5cm]{apple.png}
      \caption{林檎の図}
    \end{figure}
        \begin{figure}
      \centering
      \includegraphics[width=5cm]{orange.png}
      \caption{林檎の図}
    \end{figure}

mkpdf は以下のファイルを生成し platex -> dvipdfmx を実行します．

* apple.bb
* orange.bb
