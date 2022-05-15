if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrMKN/id.git /id     
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /id
fi
cd /id
pip3 install -U -r requirements.txt
echo "BOT IS STARTING⚡️⚡️⚡️"
python3 mkn.py
