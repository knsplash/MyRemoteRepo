sphinx-apidoc -f -o source ..
del /q build\generated
sphinx-build source build
build\index.html
