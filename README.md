source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

source venv/bin/activate

pip install Pillow
pip install numpy

pip install flake8
alias norminette=flake8

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python rotate.py

deactivate

rm -rf __pycache__
rm -rf venv

