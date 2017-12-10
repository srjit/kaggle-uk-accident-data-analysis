(TeX-add-style-hook
 "report"
 (lambda ()
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "neu_handout"
    "neu_handout10"
    "url"
    "amssymb"
    "amsmath"
    "marvosym"
    "hyperref"
    "enumitem"
    "graphicx"
    "subcaption"
    "caption"
    "comment")
   (LaTeX-add-labels
    "fig:frequency"
    "fig:hour-study"
    "fig:day_study"))
 :latex)

