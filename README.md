# Intoduction #

The project provide a platform independent calculator. Nothing super fancy

# Installation

```
pip install -i https://test.pypi.org/simple/ pancalc
```

# Usage

```
pancalc 3+4 # output 7
pancalc 2+2 # 4
pancalc (2+2) # 4
pancalc (2 + 2) #4
pancalc (2**2) # 4
pancalc --variable X 2 X**2 # 4
pancalc --force-float --variable X 2 X**2 # 4.0
pancalc --variable X 2.0 X**2 # 4.0
pancalc --force-int -V X 2.0 X**2 # 4
```

# For the developer

```
pip install -i https://test.pypi.org/simple/ pmake
pmake build install 
pmake upload-to-test-pypi
```