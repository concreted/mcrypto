# Prerequisites
sudo apt-get update
sudo apt-get -y install python-dev

# Install Pycrypto
cd ~/Downloads
wget -N -r https://pypi.python.org/packages/source/p/pycrypto/pycrypto-2.6.1.tar.gz
tar -xzvf pycrypto-2.6.1.tar.gz
cd pycrypto-2.6.1
python setup.py build
python setup.py install
python setup.py test