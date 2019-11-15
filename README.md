# RPM Spec and Build for Weave Net

# Building

The RPMs may be built with [Docker](#with-docker), [Vagrant](#with-vagrant), or [manual](#manual).

Whatever way you choose you will need to do a few basic things first.

```bash
git clone https://github.com/myENA/weave-rpm  ## check out this code
cd weave-rpm                                  ## uhh... you should know
mkdir -p artifacts                            ## prep the artifacts location
```

## With Docker

```bash
docker build -t ena/weave-rpm .                                ## build the image
docker run -v $PWD/artifacts:/tmp/artifacts -it ena/weave-rpm  ## run the image and build the RPMs
```

## With Vagrant

```bash
vagrant up                         ## provision and build the RPMs
```

## Manual

```bash
cat build.sh     ## read the script
```
## Result

Your RPMs and SRPMs will be copied to the `artifacts` folder.  Congratulations.  You just built RPMs in a controlled environment in an easily reproducible manner.
