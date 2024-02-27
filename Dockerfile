FROM python:3.10-slim
WORKDIR /build
COPY ./requirements.txt .
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y curl gcc git && \
    pip install --upgrade pip setuptools wheel && \
    cd /usr/local/src/ && \
    git clone https://github.com/WiringPi/WiringPi.git && \
    cd WiringPi && \
    cat <<'PATCH' | patch --ignore-whitespace -p1 wiringPi/wiringPi.c \
    @@ -747,6 +747,7 @@ int piGpioLayout (void) \
      if ((cpuFd = fopen ("/proc/cpuinfo", "r")) == NULL) \
         piGpioLayoutOops ("Unable to open /proc/cpuinfo") ; \
    +#ifdef DONT_CARE_ANYMORE \
     // Start by looking for the Architecture to make sure we're really running \
     // on a Pi. I'm getting fed-up with people whinging at me because \
     // they can't get it to work on weirdFruitPi boards... \
    @@ -769,7 +770,6 @@ int piGpioLayout (void) \
     // I do not support so don't email me your bleating whinges about anything \
     // other than a genuine Raspberry Pi. \
    \
    -#ifdef DONT_CARE_ANYMORE \
       if (! (strstr (line, "BCM2708") || strstr (line, "BCM2709") || strstr (line, "BCM2835"))) \
       { \
         fprintf (stderr, "Unable to determine hardware version. I see: %s,\n", line) ; \
    PATCH

RUN pip install -r requirements.txt
WORKDIR /app
CMD python main.py