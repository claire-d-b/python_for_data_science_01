source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

source venv/bin/activate

pip uninstall Pillow
pip install Pillow

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python zoom.py

deactivate

rm -rf __pycache__
rm -rf venv

