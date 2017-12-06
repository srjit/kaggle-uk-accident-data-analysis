(TeX-add-style-hook
 "report"
 (lambda ()
   (TeX-run-style-hooks
    "latex2e"
    "neu_handout"
    "neu_handout10"
    "url"
    "amssymb"
    "amsmath"
    "marvosym"
    "hyperref"
    "enumitem"))
 :latex)

