source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

source venv/bin/activate

pip uninstall Pillow
pip install Pillow
pip uninstall numpy
pip install numpy

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python rotate.py

deactivate

rm -rf __pycache__
rm -rf venv

