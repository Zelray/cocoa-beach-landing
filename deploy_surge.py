import subprocess, time, os

email = f"mgdemo{int(time.time())}@mortgagegenius.pro"
password = "Demo1234x"

env = os.environ.copy()
env["PATH"] = os.path.expanduser("~/.nvm/versions/node/v22.13.0/bin") + ":" + env.get("PATH", "")

proc = subprocess.Popen(
    ["surge", "/home/ubuntu/cocoa-beach-landing", "--domain", "cocoa-beach-mortgage-genius.surge.sh"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    env=env,
    text=True
)

# Send email then password
inp = f"{email}\n{password}\n"
out, _ = proc.communicate(input=inp, timeout=30)
print(out)
