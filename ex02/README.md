source ~/.zshrc
python -m venv venv
source venv/bin/activate
pip install --upgrade pip

echo alias python='./venv/bin/python' >> venv/bin/activate

deactivate
source venv/bin/activate

pip uninstall Pillow
pip install Pillow

echo alias python='./venv/bin/python' >> venv/bin/activate
source venv/bin/activate

python tester.py

deactivate

