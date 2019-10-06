# BatteryTracker

For reasons of losing the previous battery of my notebook, I want to try to take more care of my new battery. The first step to do that is to stop charging when the battery level reaches 80%. To do that it was created a BatteryTracker script that sends a notification on Ubuntu if the battery level is above 80% and the notebook is plugged.

First setup the BatteryTracker virtualenv with:

```bash
$ virtualenv -p python3 py3env
```

Then install `psutil` to do the battery check


```bash
source ~/py3env/bin/activate
pip install psutil
```

With that done all there is left is to set a cronjob to check the battery level every 5 minutes. To set the user cronjob one should open the crontab with:

```bash
$ crontab -e
```

and add the line

```bash
*/5 * * * * ~/py3env/bin/python /path/to/BatteryTracker.py
```
