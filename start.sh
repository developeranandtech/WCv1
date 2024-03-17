echo "Cloning Repo, Please Wait..."
git clone -b main https://github.com/akashanandtech/WCv1.git /WCv1
cd /WCv1
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
