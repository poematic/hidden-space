\* Bin auf WSL umgestiegen, da es **Triton für Windows nicht unbedingt gibt**

\* Da es mit dem nighty torch-Installationsbefehl Probleme gegeben hat, und weil die frühere Triton Version **wahrscheinlicher mit PyTorch 2.6. funktioniert**, habe ich diesen traditionelleren Befehl verwendet:

pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu126

\* Dann das abgeänderte specific\_requirements-no\_torch-old-triton.txt installieren

\* Hierbei gab es Probleme mit dem **adam\_atan2** package. Dieses wurde zwar installiert, **aber eine CUDA-Erweiterung wurde nicht automatisch kompiliert. Mit dem zusätzlich installierten nvcc wurde das schließlich gemacht**. Es mussten aber auch noch zusätzliche Feinheiten erledigt werden (siehe ChatGPT Unterhaltung "TRM Tokenisierung erklärt"). 

\* Der vorletzte Befehl war nicht mehr nötig

\* Anstatt des letzten einfach 

wandb login 

aufrufen, um zu vermeiden, den Key in Bash zu kopieren.



(base) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ conda create -n TRM python=3.10

conda activate TRM

Channels:

&#x20;- defaults

Platform: linux-64

Collecting package metadata (repodata.json): done

Solving environment: done





TERMINAL HISTORY

\## Package Plan ##



&#x20; environment location: /home/mathi/miniconda3/envs/TRM



&#x20; added / updated specs:

&#x20;   - python=3.10





The following NEW packages will be INSTALLED:



&#x20; \_libgcc\_mutex      pkgs/main/linux-64::\_libgcc\_mutex-0.1-main

&#x20; \_openmp\_mutex      pkgs/main/linux-64::\_openmp\_mutex-5.1-52\_gnu

&#x20; bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b\_6

&#x20; ca-certificates    pkgs/main/noarch::ca-certificates-2026.10.20-h59cdc77\_1

&#x20; ld\_impl\_linux-64   pkgs/main/linux-64::ld\_impl\_linux-64-2.44-h9e0c5a2\_3

&#x20; libexpat           pkgs/main/linux-64::libexpat-2.10.0-h7354ed3\_0

&#x20; libffi             pkgs/main/linux-64::libffi-3.4.8-h06d3fd0\_3

&#x20; libgcc             pkgs/main/linux-64::libgcc-15.2.0-h69a1729\_8

&#x20; libgcc-ng          pkgs/main/linux-64::libgcc-ng-15.2.0-h166f726\_8

&#x20; libnsl             pkgs/main/linux-64::libnsl-2.0.0-h5eee18b\_0

&#x20; libstdcxx          pkgs/main/linux-64::libstdcxx-15.2.0-h39759b7\_8

&#x20; libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b\_0

&#x20; libxcb             pkgs/main/linux-64::libxcb-1.17.0-h9b100fa\_0

&#x20; libzlib            pkgs/main/linux-64::libzlib-1.3.2-h47b2149\_0

&#x20; ncurses            pkgs/main/linux-64::ncurses-6.6-hfaaeb4e\_0

&#x20; openssl            pkgs/main/linux-64::openssl-3.5.9-h1b28b03\_0

&#x20; packaging          pkgs/main/linux-64::packaging-26.3-py310h06a4308\_0

&#x20; pip                pkgs/main/noarch::pip-26.2.2-pyhc872135\_0

&#x20; pthread-stubs      pkgs/main/linux-64::pthread-stubs-0.3-h47b2149\_2

&#x20; python             pkgs/main/linux-64::python-3.10.22-hd9cb797\_1

&#x20; readline           pkgs/main/linux-64::readline-8.3-hc2a1206\_0

&#x20; setuptools         pkgs/main/linux-64::setuptools-84.2.1-py310h06a4308\_0

&#x20; sqlite             pkgs/main/linux-64::sqlite-3.53.4-h795bf6d\_0

&#x20; tk                 pkgs/main/linux-64::tk-8.6.15-h54e0aa7\_0

&#x20; tzdata             pkgs/main/noarch::tzdata-2026c-he532380\_0

&#x20; wheel              pkgs/main/linux-64::wheel-0.48.0-py310h06a4308\_0

&#x20; xorg-libx11        pkgs/main/linux-64::xorg-libx11-1.8.14-h65de747\_0

&#x20; xorg-libxau        pkgs/main/linux-64::xorg-libxau-1.0.12-h9b100fa\_0

&#x20; xorg-libxdmcp      pkgs/main/linux-64::xorg-libxdmcp-1.1.5-h9b100fa\_0

&#x20; xorg-xorgproto     pkgs/main/linux-64::xorg-xorgproto-2025.1-h47b2149\_0

&#x20; xz                 pkgs/main/linux-64::xz-5.8.4-h140a991\_0

&#x20; zlib               pkgs/main/linux-64::zlib-1.3.2-h47b2149\_0





Proceed (\[y]/n)? y





Downloading and Extracting Packages:



Preparing transaction: done

Verifying transaction: done

Executing transaction: done

\#

\# To activate this environment, use

\#

\#     $ conda activate TRM

\#

\# To deactivate an active environment, use

\#

\#     $ conda deactivate



(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ pip install --upgrade pip wheel setuptools

Requirement already satisfied: pip in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (26.2.2)

Collecting pip

&#x20; Using cached pip-26.3-py3-none-any.whl.metadata (4.6 kB)

Requirement already satisfied: wheel in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (0.48.0)

Requirement already satisfied: setuptools in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (84.2.1)

Requirement already satisfied: packaging>=24.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wheel) (26.3)

Using cached pip-26.3-py3-none-any.whl (2.0 MB)

Installing collected packages: pip

&#x20; Attempting uninstall: pip

&#x20;   Found existing installation: pip 26.2.2

&#x20;   Uninstalling pip-26.2.2:

&#x20;     Successfully uninstalled pip-26.2.2

Successfully installed pip-26.3

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu126

Looking in indexes: https://download.pytorch.org/whl/cu126

Collecting torch==2.6.0

&#x20; Downloading torch-2.6.0%2Bcu126-cp310-cp310-manylinux\_2\_28\_x86\_64.whl.metadata (28 kB)

Collecting torchvision==0.21.0

&#x20; Downloading torchvision-0.21.0%2Bcu126-cp310-cp310-linux\_x86\_64.whl.metadata (6.1 kB)

Collecting torchaudio==2.6.0

&#x20; Downloading torchaudio-2.6.0%2Bcu126-cp310-cp310-linux\_x86\_64.whl.metadata (6.6 kB)

Collecting filelock (from torch==2.6.0)

&#x20; Using cached filelock-4.1.0-py3-none-any.whl.metadata (2.0 kB)

Collecting typing-extensions>=4.10.0 (from torch==2.6.0)

&#x20; Using cached typing\_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)

Collecting sympy==1.13.1 (from torch==2.6.0)

&#x20; Downloading sympy-1.13.1-py3-none-any.whl.metadata (12 kB)

Collecting networkx (from torch==2.6.0)

&#x20; Using cached networkx-3.4.2-py3-none-any.whl.metadata (6.3 kB)

Collecting jinja2 (from torch==2.6.0)

&#x20; Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)

Collecting fsspec (from torch==2.6.0)

&#x20; Using cached fsspec-2026.9.0-py3-none-any.whl.metadata (10 kB)

Collecting nvidia-cuda-nvrtc-cu12==12.6.77 (from torch==2.6.0)

&#x20; Downloading nvidia\_cuda\_nvrtc\_cu12-12.6.77-py3-none-manylinux2014\_x86\_64.whl (23.7 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 23.7/23.7 MB 52.4 MB/s  0:00:00

Collecting nvidia-cuda-runtime-cu12==12.6.77 (from torch==2.6.0)

&#x20; Downloading nvidia\_cuda\_runtime\_cu12-12.6.77-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (897 kB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 897.7/897.7 kB 86.5 MB/s  0:00:00

Collecting nvidia-cuda-cupti-cu12==12.6.80 (from torch==2.6.0)

&#x20; Downloading nvidia\_cuda\_cupti\_cu12-12.6.80-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (8.9 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 MB 52.5 MB/s  0:00:00

Collecting nvidia-cudnn-cu12==9.5.1.17 (from torch==2.6.0)

&#x20; Downloading nvidia\_cudnn\_cu12-9.5.1.17-py3-none-manylinux\_2\_28\_x86\_64.whl (571.0 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 571.0/571.0 MB 21.6 MB/s  0:00:25

Collecting nvidia-cublas-cu12==12.6.4.1 (from torch==2.6.0)

&#x20; Downloading nvidia\_cublas\_cu12-12.6.4.1-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (393.1 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 393.1/393.1 MB 21.8 MB/s  0:00:16

Collecting nvidia-cufft-cu12==11.3.0.4 (from torch==2.6.0)

&#x20; Downloading nvidia\_cufft\_cu12-11.3.0.4-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (200.2 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 200.2/200.2 MB 24.3 MB/s  0:00:08

Collecting nvidia-curand-cu12==10.3.7.77 (from torch==2.6.0)

&#x20; Downloading nvidia\_curand\_cu12-10.3.7.77-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (56.3 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 56.3/56.3 MB 26.7 MB/s  0:00:02

Collecting nvidia-cusolver-cu12==11.7.1.2 (from torch==2.6.0)

&#x20; Downloading nvidia\_cusolver\_cu12-11.7.1.2-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (158.2 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 158.2/158.2 MB 22.6 MB/s  0:00:06

Collecting nvidia-cusparse-cu12==12.5.4.2 (from torch==2.6.0)

&#x20; Downloading nvidia\_cusparse\_cu12-12.5.4.2-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (216.6 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 216.6/216.6 MB 22.7 MB/s  0:00:09

Collecting nvidia-cusparselt-cu12==0.6.3 (from torch==2.6.0)

&#x20; Downloading nvidia\_cusparselt\_cu12-0.6.3-py3-none-manylinux2014\_x86\_64.whl (156.8 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 156.8/156.8 MB 24.6 MB/s  0:00:06

Collecting nvidia-nccl-cu12==2.21.5 (from torch==2.6.0)

&#x20; Downloading nvidia\_nccl\_cu12-2.21.5-py3-none-manylinux2014\_x86\_64.whl (188.7 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 188.7/188.7 MB 22.9 MB/s  0:00:08

Collecting nvidia-nvtx-cu12==12.6.77 (from torch==2.6.0)

&#x20; Downloading nvidia\_nvtx\_cu12-12.6.77-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (89 kB)

Collecting nvidia-nvjitlink-cu12==12.6.85 (from torch==2.6.0)

&#x20; Downloading nvidia\_nvjitlink\_cu12-12.6.85-py3-none-manylinux2010\_x86\_64.manylinux\_2\_12\_x86\_64.whl (19.7 MB)

&#x20;    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.7/19.7 MB 28.8 MB/s  0:00:00

Collecting triton==3.2.0 (from torch==2.6.0)

&#x20; Downloading triton-3.2.0-cp310-cp310-manylinux\_2\_27\_x86\_64.manylinux\_2\_28\_x86\_64.whl.metadata (1.4 kB)

Collecting numpy (from torchvision==0.21.0)

&#x20; Using cached numpy-2.2.6-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl.metadata (62 kB)

Collecting pillow!=8.3.\*,>=5.3.0 (from torchvision==0.21.0)

&#x20; Downloading pillow-12.3.0-cp310-cp310-manylinux\_2\_27\_x86\_64.manylinux\_2\_28\_x86\_64.whl.metadata (9.1 kB)

Collecting mpmath<1.4,>=1.1.0 (from sympy==1.13.1->torch==2.6.0)

&#x20; Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)

Collecting MarkupSafe>=2.0 (from jinja2->torch==2.6.0)

&#x20; Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl.metadata (2.7 kB)

Downloading torch-2.6.0%2Bcu126-cp310-cp310-manylinux\_2\_28\_x86\_64.whl (764.6 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 764.6/764.6 MB 16.8 MB/s  0:01:03

Downloading torchvision-0.21.0%2Bcu126-cp310-cp310-linux\_x86\_64.whl (7.3 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 11.6 MB/s  0:00:00

Downloading torchaudio-2.6.0%2Bcu126-cp310-cp310-linux\_x86\_64.whl (3.4 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 32.6 MB/s  0:00:00

Downloading sympy-1.13.1-py3-none-any.whl (6.2 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.2/6.2 MB 7.5 MB/s  0:00:00

Downloading triton-3.2.0-cp310-cp310-manylinux\_2\_27\_x86\_64.manylinux\_2\_28\_x86\_64.whl (166.6 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 166.6/166.6 MB 26.4 MB/s  0:00:06

Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 6.4 MB/s  0:00:00

Downloading pillow-12.3.0-cp310-cp310-manylinux\_2\_27\_x86\_64.manylinux\_2\_28\_x86\_64.whl (6.9 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.9/6.9 MB 12.8 MB/s  0:00:00

Downloading typing\_extensions-4.16.0-py3-none-any.whl (45 kB)

Downloading filelock-4.1.0-py3-none-any.whl (133 kB)

Downloading fsspec-2026.9.0-py3-none-any.whl (221 kB)

Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)

Downloading markupsafe-3.0.3-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl (20 kB)

Downloading networkx-3.4.2-py3-none-any.whl (1.7 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.7/1.7 MB 15.6 MB/s  0:00:00

Downloading numpy-2.2.6-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl (16.8 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 24.2 MB/s  0:00:00

Installing collected packages: triton, nvidia-cusparselt-cu12, mpmath, typing-extensions, sympy, pillow, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, MarkupSafe, fsspec, filelock, nvidia-cusparse-cu12, nvidia-cufft-cu12, nvidia-cudnn-cu12, jinja2, nvidia-cusolver-cu12, torch, torchvision, torchaudio

Successfully installed MarkupSafe-3.0.3 filelock-4.1.0 fsspec-2026.9.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.4.2 numpy-2.2.6 nvidia-cublas-cu12-12.6.4.1 nvidia-cuda-cupti-cu12-12.6.80 nvidia-cuda-nvrtc-cu12-12.6.77 nvidia-cuda-runtime-cu12-12.6.77 nvidia-cudnn-cu12-9.5.1.17 nvidia-cufft-cu12-11.3.0.4 nvidia-curand-cu12-10.3.7.77 nvidia-cusolver-cu12-11.7.1.2 nvidia-cusparse-cu12-12.5.4.2 nvidia-cusparselt-cu12-0.6.3 nvidia-nccl-cu12-2.21.5 nvidia-nvjitlink-cu12-12.6.85 nvidia-nvtx-cu12-12.6.77 pillow-12.3.0 sympy-1.13.1 torch-2.6.0+cu126 torchaudio-2.6.0+cu126 torchvision-0.21.0+cu126 triton-3.2.0 typing-extensions-4.16.0

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ python -c "import torch; print(torch.cuda.is\_available())"

True

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ pip install -r requirements-no\_torch.txt

ERROR: Could not open requirements file: \[Errno 2] No such file or directory: 'requirements-no\_torch.txt'

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ pip install -r specific\_requirements-no\_torch.txt

Collecting adam-atan2==0.0.3 (from -r specific\_requirements-no\_torch.txt (line 1))

&#x20; Downloading adam\_atan2-0.0.3.tar.gz (11 kB)

&#x20; Installing build dependencies ... done

&#x20; Getting requirements to build wheel ... done

&#x20; Installing backend dependencies ... done

&#x20; Preparing metadata (pyproject.toml) ... done

Collecting einops==0.8.1 (from -r specific\_requirements-no\_torch.txt (line 2))

&#x20; Downloading einops-0.8.1-py3-none-any.whl.metadata (13 kB)

WARNING: Cache entry deserialization failed, entry ignored

WARNING: Cache entry deserialization failed, entry ignored

Collecting tqdm==4.67.1 (from -r specific\_requirements-no\_torch.txt (line 3))

&#x20; Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)

Collecting coolname==2.2.0 (from -r specific\_requirements-no\_torch.txt (line 4))

&#x20; Downloading coolname-2.2.0-py2.py3-none-any.whl.metadata (6.2 kB)

Collecting pydantic==2.11.7 (from -r specific\_requirements-no\_torch.txt (line 5))

&#x20; Downloading pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)

Collecting argdantic==1.3.3 (from -r specific\_requirements-no\_torch.txt (line 6))

&#x20; Downloading argdantic-1.3.3-py2.py3-none-any.whl.metadata (7.2 kB)

Collecting wandb==0.21.3 (from -r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading wandb-0.21.3-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl.metadata (10 kB)

Collecting omegaconf==2.3.0 (from -r specific\_requirements-no\_torch.txt (line 8))

&#x20; Downloading omegaconf-2.3.0-py3-none-any.whl.metadata (3.9 kB)

Collecting hydra-core==1.3.2 (from -r specific\_requirements-no\_torch.txt (line 9))

&#x20; Downloading hydra\_core-1.3.2-py3-none-any.whl.metadata (5.5 kB)

Collecting huggingface\_hub==0.34.4 (from -r specific\_requirements-no\_torch.txt (line 10))

&#x20; Downloading huggingface\_hub-0.34.4-py3-none-any.whl.metadata (14 kB)

Collecting packaging==24.1 (from -r specific\_requirements-no\_torch.txt (line 11))

&#x20; Downloading packaging-24.1-py3-none-any.whl.metadata (3.2 kB)

Collecting ninja==1.13.0 (from -r specific\_requirements-no\_torch.txt (line 12))

&#x20; Downloading ninja-1.13.0-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl.metadata (5.1 kB)

Collecting wheel==0.45.1 (from -r specific\_requirements-no\_torch.txt (line 13))

&#x20; Downloading wheel-0.45.1-py3-none-any.whl.metadata (2.3 kB)

Collecting setuptools==80.9.0 (from -r specific\_requirements-no\_torch.txt (line 14))

&#x20; Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)

Collecting setuptools-scm==9.2.0 (from -r specific\_requirements-no\_torch.txt (line 15))

&#x20; Downloading setuptools\_scm-9.2.0-py3-none-any.whl.metadata (7.7 kB)

Collecting pydantic-core==2.33.2 (from -r specific\_requirements-no\_torch.txt (line 16))

&#x20; Downloading pydantic\_core-2.33.2-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl.metadata (6.8 kB)

Collecting numba==0.61.2 (from -r specific\_requirements-no\_torch.txt (line 18))

&#x20; Downloading numba-0.61.2-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl.metadata (2.8 kB)

Requirement already satisfied: triton==3.2.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from -r specific\_requirements-no\_torch.txt (line 19)) (3.2.0)

Collecting annotated-types>=0.6.0 (from pydantic==2.11.7->-r specific\_requirements-no\_torch.txt (line 5))

&#x20; Downloading annotated\_types-0.8.0-py3-none-any.whl.metadata (15 kB)

Requirement already satisfied: typing-extensions>=4.12.2 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from pydantic==2.11.7->-r specific\_requirements-no\_torch.txt (line 5)) (4.16.0)

Collecting typing-inspection>=0.4.0 (from pydantic==2.11.7->-r specific\_requirements-no\_torch.txt (line 5))

&#x20; Downloading typing\_inspection-0.4.5-py3-none-any.whl.metadata (2.6 kB)

Collecting pydantic-settings<3,>=2.4.0 (from argdantic==1.3.3->-r specific\_requirements-no\_torch.txt (line 6))

&#x20; Downloading pydantic\_settings-2.15.0-py3-none-any.whl.metadata (3.9 kB)

Collecting click>=8.0.1 (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading click-8.5.1-py3-none-any.whl.metadata (2.6 kB)

Collecting gitpython!=3.1.29,>=1.0.0 (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading gitpython-3.2.1-py3-none-any.whl.metadata (13 kB)

Collecting platformdirs (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading platformdirs-4.12.4-py3-none-any.whl.metadata (5.5 kB)

Collecting protobuf!=4.21.0,!=5.28.0,<7,>=3.19.0 (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading protobuf-6.33.6-cp39-abi3-manylinux2014\_x86\_64.whl.metadata (593 bytes)

Collecting pyyaml (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl.metadata (2.4 kB)

Collecting requests<3,>=2.0.0 (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)

Collecting sentry-sdk>=2.0.0 (from wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading sentry\_sdk-2.74.0-py3-none-any.whl.metadata (11 kB)

Collecting antlr4-python3-runtime==4.9.\* (from omegaconf==2.3.0->-r specific\_requirements-no\_torch.txt (line 8))

&#x20; Downloading antlr4-python3-runtime-4.9.3.tar.gz (117 kB)

&#x20; Installing build dependencies ... done

&#x20; Getting requirements to build wheel ... done

&#x20; Preparing metadata (pyproject.toml) ... done

Requirement already satisfied: filelock in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from huggingface\_hub==0.34.4->-r specific\_requirements-no\_torch.txt (line 10)) (4.1.0)

Requirement already satisfied: fsspec>=2023.5.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from huggingface\_hub==0.34.4->-r specific\_requirements-no\_torch.txt (line 10)) (2026.9.0)

Collecting hf-xet<2.0.0,>=1.1.3 (from huggingface\_hub==0.34.4->-r specific\_requirements-no\_torch.txt (line 10))

&#x20; Downloading hf\_xet-1.8.0-cp38-abi3-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl.metadata (4.9 kB)

Collecting tomli>=1 (from setuptools-scm==9.2.0->-r specific\_requirements-no\_torch.txt (line 15))

&#x20; Using cached tomli-2.5.0-py3-none-any.whl.metadata (10 kB)

Collecting llvmlite<0.45,>=0.44.0dev0 (from numba==0.61.2->-r specific\_requirements-no\_torch.txt (line 18))

&#x20; Downloading llvmlite-0.44.0-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl.metadata (4.8 kB)

Requirement already satisfied: numpy<2.3,>=1.24 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from numba==0.61.2->-r specific\_requirements-no\_torch.txt (line 18)) (2.2.6)

Collecting python-dotenv>=0.21.0 (from pydantic-settings<3,>=2.4.0->argdantic==1.3.3->-r specific\_requirements-no\_torch.txt (line 6))

&#x20; Downloading python\_dotenv-1.2.4-py3-none-any.whl.metadata (29 kB)

Collecting charset\_normalizer<4,>=2 (from requests<3,>=2.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading charset\_normalizer-3.5.2-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl.metadata (46 kB)

Collecting idna<4,>=2.5 (from requests<3,>=2.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading idna-3.20-py3-none-any.whl.metadata (7.2 kB)

Collecting urllib3<3,>=1.26 (from requests<3,>=2.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading urllib3-2.8.0-py3-none-any.whl.metadata (7.4 kB)

Collecting certifi>=2023.5.7 (from requests<3,>=2.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading certifi-2026.10.23-py3-none-any.whl.metadata (2.5 kB)

Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.29,>=1.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading gitdb-4.0.12-py3-none-any.whl.metadata (1.2 kB)

Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.29,>=1.0.0->wandb==0.21.3->-r specific\_requirements-no\_torch.txt (line 7))

&#x20; Downloading smmap-5.0.3-py3-none-any.whl.metadata (4.6 kB)

Downloading einops-0.8.1-py3-none-any.whl (64 kB)

Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)

Downloading coolname-2.2.0-py2.py3-none-any.whl (37 kB)

Downloading pydantic-2.11.7-py3-none-any.whl (444 kB)

Downloading argdantic-1.3.3-py2.py3-none-any.whl (26 kB)

Downloading wandb-0.21.3-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl (19.6 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.6/19.6 MB 34.9 MB/s  0:00:00

Downloading omegaconf-2.3.0-py3-none-any.whl (79 kB)

Downloading hydra\_core-1.3.2-py3-none-any.whl (154 kB)

Downloading huggingface\_hub-0.34.4-py3-none-any.whl (561 kB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 561.5/561.5 kB 14.9 MB/s  0:00:00

Downloading packaging-24.1-py3-none-any.whl (53 kB)

Downloading ninja-1.13.0-py3-none-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (180 kB)

Downloading wheel-0.45.1-py3-none-any.whl (72 kB)

Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 16.2 MB/s  0:00:00

Downloading setuptools\_scm-9.2.0-py3-none-any.whl (62 kB)

Downloading pydantic\_core-2.33.2-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl (2.0 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.0/2.0 MB 49.9 MB/s  0:00:00

Downloading numba-0.61.2-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (3.8 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.8/3.8 MB 47.5 MB/s  0:00:00

Downloading hf\_xet-1.8.0-cp38-abi3-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.whl (4.3 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 4.3/4.3 MB 54.1 MB/s  0:00:00

Downloading llvmlite-0.44.0-cp310-cp310-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl (42.4 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.4/42.4 MB 62.9 MB/s  0:00:00

Downloading protobuf-6.33.6-cp39-abi3-manylinux2014\_x86\_64.whl (323 kB)

Downloading pydantic\_settings-2.15.0-py3-none-any.whl (69 kB)

Downloading requests-2.34.2-py3-none-any.whl (73 kB)

Downloading charset\_normalizer-3.5.2-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl (271 kB)

Downloading idna-3.20-py3-none-any.whl (69 kB)

Downloading urllib3-2.8.0-py3-none-any.whl (135 kB)

Downloading annotated\_types-0.8.0-py3-none-any.whl (13 kB)

Downloading certifi-2026.10.23-py3-none-any.whl (135 kB)

Downloading click-8.5.1-py3-none-any.whl (126 kB)

Downloading gitpython-3.2.1-py3-none-any.whl (231 kB)

Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)

Downloading smmap-5.0.3-py3-none-any.whl (24 kB)

Downloading python\_dotenv-1.2.4-py3-none-any.whl (23 kB)

Downloading pyyaml-6.0.3-cp310-cp310-manylinux2014\_x86\_64.manylinux\_2\_17\_x86\_64.manylinux\_2\_28\_x86\_64.whl (770 kB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 770.3/770.3 kB 23.0 MB/s  0:00:00

Downloading sentry\_sdk-2.74.0-py3-none-any.whl (549 kB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 549.8/549.8 kB 17.7 MB/s  0:00:00

Using cached tomli-2.5.0-py3-none-any.whl (14 kB)

Downloading typing\_inspection-0.4.5-py3-none-any.whl (14 kB)

Downloading platformdirs-4.12.4-py3-none-any.whl (32 kB)

Building wheels for collected packages: adam-atan2, antlr4-python3-runtime

&#x20; Building wheel for adam-atan2 (pyproject.toml) ... done

&#x20; Created wheel for adam-atan2: filename=adam\_atan2-0.0.3-py3-none-any.whl size=8683 sha256=4d7ba9ab9af0b61d991c9be4ed162c599e6c902c1e5ce54d1ee3fb3eaf3c296d

&#x20; Stored in directory: /home/mathi/.cache/pip/wheels/8e/79/b9/e3edcc5f7812e0e4f909654fb6b39950854a66042fd2f84424

&#x20; Building wheel for antlr4-python3-runtime (pyproject.toml) ... done

&#x20; Created wheel for antlr4-python3-runtime: filename=antlr4\_python3\_runtime-4.9.3-py3-none-any.whl size=144590 sha256=f4d8e61141f46f65dbd48d823878429e781a571296a70523010fb5d365e04c68

&#x20; Stored in directory: /home/mathi/.cache/pip/wheels/12/93/dd/1f6a127edc45659556564c5730f6d4e300888f4bca2d4c5a88

Successfully built adam-atan2 antlr4-python3-runtime

Installing collected packages: coolname, antlr4-python3-runtime, adam-atan2, wheel, urllib3, typing-inspection, tqdm, tomli, smmap, setuptools, pyyaml, python-dotenv, pydantic-core, protobuf, platformdirs, packaging, ninja, llvmlite, idna, hf-xet, einops, click, charset\_normalizer, certifi, annotated-types, setuptools-scm, sentry-sdk, requests, pydantic, omegaconf, numba, gitdb, pydantic-settings, hydra-core, huggingface\_hub, gitpython, wandb, argdantic

&#x20; Attempting uninstall: wheel

&#x20;   Found existing installation: wheel 0.48.0

&#x20;   Uninstalling wheel-0.48.0:

&#x20;     Successfully uninstalled wheel-0.48.0

&#x20; Attempting uninstall: setuptools

&#x20;   Found existing installation: setuptools 84.2.1

&#x20;   Uninstalling setuptools-84.2.1:

&#x20;     Successfully uninstalled setuptools-84.2.1

&#x20; Attempting uninstall: packaging

&#x20;   Found existing installation: packaging 26.3

&#x20;   Uninstalling packaging-26.3:

&#x20;     Successfully uninstalled packaging-26.3

Successfully installed adam-atan2-0.0.3 annotated-types-0.8.0 antlr4-python3-runtime-4.9.3 argdantic-1.3.3 certifi-2026.10.23 charset\_normalizer-3.5.2 click-8.5.1 coolname-2.2.0 einops-0.8.1 gitdb-4.0.12 gitpython-3.2.1 hf-xet-1.8.0 huggingface\_hub-0.34.4 hydra-core-1.3.2 idna-3.20 llvmlite-0.44.0 ninja-1.13.0 numba-0.61.2 omegaconf-2.3.0 packaging-24.1 platformdirs-4.12.4 protobuf-6.33.6 pydantic-2.11.7 pydantic-core-2.33.2 pydantic-settings-2.15.0 python-dotenv-1.2.4 pyyaml-6.0.3 requests-2.34.2 sentry-sdk-2.74.0 setuptools-80.9.0 setuptools-scm-9.2.0 smmap-5.0.3 tomli-2.5.0 tqdm-4.67.1 typing-inspection-0.4.5 urllib3-2.8.0 wandb-0.21.3 wheel-0.45.1

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ python -c "import torch; print(torch.cuda.is\_available())"

True

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ python -c "import adam\_atan2; print('Import erfolgreich')

>

> ^C

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ python -c "import adam\_atan2; print('Import erfolgreich')"

Traceback (most recent call last):

&#x20; File "<string>", line 1, in <module>

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/adam\_atan2/\_\_init\_\_.py", line 1, in <module>

&#x20;   from .adam\_atan2 import AdamATan2

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/adam\_atan2/adam\_atan2.py", line 4, in <module>

&#x20;   import adam\_atan2\_backend

ModuleNotFoundError: No module named 'adam\_atan2\_backend'

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ nvcc --version

Command 'nvcc' not found, but can be installed with:

sudo apt install nvidia-cuda-toolkit

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64/cuda-keyring\_1.1-1\_all.deb

\--2026-11-09 16:24:08--  https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64/cuda-keyring\_1.1-1\_all.deb

Resolving developer.download.nvidia.com (developer.download.nvidia.com)... 104.83.4.49, 104.83.4.57

Connecting to developer.download.nvidia.com (developer.download.nvidia.com)|104.83.4.49|:443... connected.

HTTP request sent, awaiting response... 200 OK

Length: 4328 (4.2K) \[application/x-deb]

Saving to: ‘cuda-keyring\_1.1-1\_all.deb’



cuda-keyring\_1.1-1 100%\[================>]   4.23K  --.-KB/s    in 0s



2026-11-09 16:24:09 (187 MB/s) - ‘cuda-keyring\_1.1-1\_all.deb’ saved \[4328/4328]



(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ sudo dpkg -i cuda-keyring\_1.1-1\_all.deb

\[sudo] password for mathi:

Sorry, try again.

\[sudo] password for mathi:

Sorry, try again.

\[sudo] password for mathi:

Selecting previously unselected package cuda-keyring.

(Reading database ... 86683 files and directories currently installed.)

Preparing to unpack cuda-keyring\_1.1-1\_all.deb ...

Unpacking cuda-keyring (1.1-1) ...

Setting up cuda-keyring (1.1-1) ...

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ sudo apt update

Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease

Hit:2 http://archive.ubuntu.com/ubuntu noble-updates InRelease

Get:3 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  InRelease \[1578 B]

Get:4 http://security.ubuntu.com/ubuntu noble-security InRelease \[126 kB]

Hit:5 http://archive.ubuntu.com/ubuntu noble-backports InRelease

Get:6 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  Packages \[2060 kB]

Hit:7 https://ppa.launchpadcontent.net/swi-prolog/stable/ubuntu noble InRelease

Get:8 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages \[1157 kB]

Get:9 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Packages \[1228 kB]

Fetched 4572 kB in 2s (2526 kB/s)

Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

243 packages can be upgraded. Run 'apt list --upgradable' to see them.

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ sudo apt install cuda-toolkit-12-6

Reading package lists... Done

Building dependency tree... Done

Reading state information... Done

The following additional packages will be installed:

&#x20; ca-certificates ca-certificates-java cuda-cccl-12-6

&#x20; cuda-command-line-tools-12-6 cuda-compiler-12-6 cuda-crt-12-6

&#x20; cuda-cudart-12-6 cuda-cudart-dev-12-6 cuda-cuobjdump-12-6

&#x20; cuda-cupti-12-6 cuda-cupti-dev-12-6 cuda-cuxxfilt-12-6

&#x20; cuda-documentation-12-6 cuda-driver-dev-12-6 cuda-gdb-12-6

&#x20; cuda-libraries-12-6 cuda-libraries-dev-12-6 cuda-nsight-12-6

&#x20; cuda-nsight-compute-12-6 cuda-nsight-systems-12-6 cuda-nvcc-12-6

&#x20; cuda-nvdisasm-12-6 cuda-nvml-dev-12-6 cuda-nvprof-12-6 cuda-nvprune-12-6

&#x20; cuda-nvrtc-12-6 cuda-nvrtc-dev-12-6 cuda-nvtx-12-6 cuda-nvvm-12-6

&#x20; cuda-nvvp-12-6 cuda-opencl-12-6 cuda-opencl-dev-12-6

&#x20; cuda-profiler-api-12-6 cuda-sanitizer-12-6

&#x20; cuda-toolkit-12-6-config-common cuda-toolkit-12-config-common

&#x20; cuda-toolkit-config-common cuda-tools-12-6 cuda-visual-tools-12-6

&#x20; default-jre default-jre-headless fonts-dejavu-extra gds-tools-12-6

&#x20; java-common libatk-wrapper-java libatk-wrapper-java-jni libcublas-12-6

&#x20; libcublas-dev-12-6 libcufft-12-6 libcufft-dev-12-6 libcufile-12-6

&#x20; libcufile-dev-12-6 libcurand-12-6 libcurand-dev-12-6 libcusolver-12-6

&#x20; libcusolver-dev-12-6 libcusparse-12-6 libcusparse-dev-12-6 libgif7

&#x20; libnpp-12-6 libnpp-dev-12-6 libnspr4 libnss3 libnvfatbin-12-6

&#x20; libnvfatbin-dev-12-6 libnvjitlink-12-6 libnvjitlink-dev-12-6

&#x20; libnvjpeg-12-6 libnvjpeg-dev-12-6 libpcsclite1 libxcb-cursor0

&#x20; libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0

&#x20; libxcb-util1 libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1

&#x20; libxkbcommon-x11-0 nsight-compute-2024.3.2 nsight-systems-2024.5.1

&#x20; openjdk-21-jre openjdk-21-jre-headless

Suggested packages:

&#x20; pcscd libnss-mdns fonts-ipafont-gothic fonts-ipafont-mincho

&#x20; fonts-wqy-microhei | fonts-wqy-zenhei fonts-indic

The following NEW packages will be installed:

&#x20; ca-certificates-java cuda-cccl-12-6 cuda-command-line-tools-12-6

&#x20; cuda-compiler-12-6 cuda-crt-12-6 cuda-cudart-12-6 cuda-cudart-dev-12-6

&#x20; cuda-cuobjdump-12-6 cuda-cupti-12-6 cuda-cupti-dev-12-6

&#x20; cuda-cuxxfilt-12-6 cuda-documentation-12-6 cuda-driver-dev-12-6

&#x20; cuda-gdb-12-6 cuda-libraries-12-6 cuda-libraries-dev-12-6

&#x20; cuda-nsight-12-6 cuda-nsight-compute-12-6 cuda-nsight-systems-12-6

&#x20; cuda-nvcc-12-6 cuda-nvdisasm-12-6 cuda-nvml-dev-12-6 cuda-nvprof-12-6

&#x20; cuda-nvprune-12-6 cuda-nvrtc-12-6 cuda-nvrtc-dev-12-6 cuda-nvtx-12-6

&#x20; cuda-nvvm-12-6 cuda-nvvp-12-6 cuda-opencl-12-6 cuda-opencl-dev-12-6

&#x20; cuda-profiler-api-12-6 cuda-sanitizer-12-6 cuda-toolkit-12-6

&#x20; cuda-toolkit-12-6-config-common cuda-toolkit-12-config-common

&#x20; cuda-toolkit-config-common cuda-tools-12-6 cuda-visual-tools-12-6

&#x20; default-jre default-jre-headless fonts-dejavu-extra gds-tools-12-6

&#x20; java-common libatk-wrapper-java libatk-wrapper-java-jni libcublas-12-6

&#x20; libcublas-dev-12-6 libcufft-12-6 libcufft-dev-12-6 libcufile-12-6

&#x20; libcufile-dev-12-6 libcurand-12-6 libcurand-dev-12-6 libcusolver-12-6

&#x20; libcusolver-dev-12-6 libcusparse-12-6 libcusparse-dev-12-6 libgif7

&#x20; libnpp-12-6 libnpp-dev-12-6 libnspr4 libnss3 libnvfatbin-12-6

&#x20; libnvfatbin-dev-12-6 libnvjitlink-12-6 libnvjitlink-dev-12-6

&#x20; libnvjpeg-12-6 libnvjpeg-dev-12-6 libpcsclite1 libxcb-cursor0

&#x20; libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0

&#x20; libxcb-util1 libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1

&#x20; libxkbcommon-x11-0 nsight-compute-2024.3.2 nsight-systems-2024.5.1

&#x20; openjdk-21-jre openjdk-21-jre-headless

The following packages will be upgraded:

&#x20; ca-certificates

1 upgraded, 84 newly installed, 0 to remove and 242 not upgraded.

Need to get 3023 MB/3024 MB of archives.

After this operation, 6790 MB of additional disk space will be used.

Do you want to continue? \[Y/n] y

Get:1 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 ca-certificates-java all 20240118ubuntu0.24.04.1 \[12.2 kB]

Get:2 http://archive.ubuntu.com/ubuntu noble/main amd64 java-common all 0.75+exp1 \[6798 B]

Get:3 http://archive.ubuntu.com/ubuntu noble/main amd64 libnspr4 amd64 2:4.35-1.1build1 \[117 kB]

Get:4 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libnss3 amd64 2:3.98-1ubuntu0.3 \[1445 kB]

Get:5 http://archive.ubuntu.com/ubuntu noble/main amd64 libpcsclite1 amd64 2.0.3-1build1 \[21.4 kB]

Get:6 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 openjdk-21-jre-headless amd64 21.0.12.1+1-1\~24.04.4 \[46.5 MB]

Get:7 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cccl-12-6 12.6.77-1 \[974 kB]

Get:8 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cupti-12-6 12.6.80-1 \[10.2 MB]

Get:9 http://archive.ubuntu.com/ubuntu noble/main amd64 default-jre-headless amd64 2:1.21-75+exp1 \[3094 B]

Get:10 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 libgif7 amd64 5.2.2-1ubuntu1.2 \[35.6 kB]

Get:11 http://archive.ubuntu.com/ubuntu noble-updates/main amd64 openjdk-21-jre amd64 21.0.12.1+1-1\~24.04.4 \[233 kB]

Get:12 http://archive.ubuntu.com/ubuntu noble/main amd64 default-jre amd64 2:1.21-75+exp1 \[922 B]

Get:13 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-xinerama0 amd64 1.15-1ubuntu2 \[5410 B]

Get:14 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-icccm4 amd64 0.4.1-1.1build3 \[10.8 kB]

Get:15 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-util1 amd64 0.4.0-1build3 \[10.7 kB]

Get:16 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-image0 amd64 0.4.0-2build1 \[10.8 kB]

Get:17 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-keysyms1 amd64 0.4.0-1build4 \[7956 B]

Get:18 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-render-util0 amd64 0.3.9-1build4 \[9608 B]

Get:19 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-xkb1 amd64 1.15-1ubuntu2 \[32.3 kB]

Get:20 http://archive.ubuntu.com/ubuntu noble/main amd64 libxkbcommon-x11-0 amd64 1.6.0-1build1 \[14.5 kB]

Get:21 http://archive.ubuntu.com/ubuntu noble/main amd64 libxcb-xinput0 amd64 1.15-1ubuntu2 \[33.2 kB]

Get:22 http://archive.ubuntu.com/ubuntu noble/universe amd64 libxcb-cursor0 amd64 0.1.4-1build1 \[10.7 kB]

Get:23 http://archive.ubuntu.com/ubuntu noble/main amd64 fonts-dejavu-extra all 2.37-8 \[1947 kB]

Get:24 http://archive.ubuntu.com/ubuntu noble/main amd64 libatk-wrapper-java all 0.40.0-3build2 \[54.3 kB]

Get:25 http://archive.ubuntu.com/ubuntu noble/main amd64 libatk-wrapper-java-jni amd64 0.40.0-3build2 \[46.4 kB]

Get:26 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cupti-dev-12-6 12.6.80-1 \[3927 kB]

Get:27 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvdisasm-12-6 12.6.77-1 \[49.9 MB]

Get:28 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cuobjdump-12-6 12.6.77-1 \[221 kB]

Get:29 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-gdb-12-6 12.6.77-1 \[25.5 MB]

Get:30 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvprof-12-6 12.6.80-1 \[2434 kB]

Get:31 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvtx-12-6 12.6.77-1 \[51.5 kB]

Get:32 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-sanitizer-12-6 12.6.77-1 \[10.1 MB]

Get:33 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-command-line-tools-12-6 12.6.3-1 \[2546 B]

Get:34 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cuxxfilt-12-6 12.6.77-1 \[191 kB]

Get:35 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-toolkit-config-common 13.5.37-1 \[21.2 kB]

Get:36 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-toolkit-12-config-common 12.9.79-1 \[16.6 kB]

Get:37 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-toolkit-12-6-config-common 12.6.77-1 \[16.5 kB]

Get:38 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cudart-12-6 12.6.77-1 \[166 kB]

Get:39 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-driver-dev-12-6 12.6.77-1 \[29.0 kB]

Get:40 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-cudart-dev-12-6 12.6.77-1 \[1026 kB]

Get:41 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvvm-12-6 12.6.85-1 \[17.9 MB]

Get:42 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-crt-12-6 12.6.85-1 \[77.4 kB]

Get:43 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvcc-12-6 12.6.85-1 \[32.6 MB]

Get:44 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvprune-12-6 12.6.77-1 \[59.4 kB]

Get:45 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-compiler-12-6 12.6.3-1 \[2510 B]

Get:46 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-documentation-12-6 12.6.77-1 \[50.0 kB]

Get:47 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvrtc-12-6 12.6.85-1 \[17.0 MB]

Get:48 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-opencl-12-6 12.6.77-1 \[24.0 kB]

Get:49 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcublas-12-6 12.6.4.1-1 \[257 MB]

Get:50 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcufft-12-6 11.3.0.4-1 \[160 MB]

Get:51 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcufile-12-6 1.11.1.6-1 \[847 kB]

Get:52 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcurand-12-6 10.3.7.77-1 \[41.4 MB]

Get:53 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcusolver-12-6 11.7.1.2-1 \[97.2 MB]

Get:54 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcusparse-12-6 12.5.4.2-1 \[120 MB]

Get:55 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnpp-12-6 12.3.1.54-1 \[93.8 MB]

Get:56 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvjitlink-12-6 12.6.85-1 \[14.7 MB]

Get:57 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvfatbin-12-6 12.6.77-1 \[734 kB]

Get:58 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvjpeg-12-6 12.3.3.54-1 \[2326 kB]

Get:59 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-libraries-12-6 12.6.3-1 \[2610 B]

Get:60 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-profiler-api-12-6 12.6.77-1 \[18.6 kB]

Get:61 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvrtc-dev-12-6 12.6.85-1 \[17.6 MB]

Get:62 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-opencl-dev-12-6 12.6.77-1 \[87.7 kB]

Get:63 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcublas-dev-12-6 12.6.4.1-1 \[277 MB]

Get:64 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcufft-dev-12-6 11.3.0.4-1 \[321 MB]

Get:65 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcufile-dev-12-6 1.11.1.6-1 \[2446 kB]

Get:66 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcurand-dev-12-6 10.3.7.77-1 \[41.7 MB]

Get:67 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcusolver-dev-12-6 11.7.1.2-1 \[66.7 MB]

Get:68 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libcusparse-dev-12-6 12.5.4.2-1 \[123 MB]

Get:69 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnpp-dev-12-6 12.3.1.54-1 \[92.4 MB]

Get:70 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvjitlink-dev-12-6 12.6.85-1 \[14.6 MB]

Get:71 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvfatbin-dev-12-6 12.6.77-1 \[607 kB]

Get:72 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  libnvjpeg-dev-12-6 12.3.3.54-1 \[2023 kB]

Get:73 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-libraries-dev-12-6 12.6.3-1 \[2654 B]

Get:74 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nsight-12-6 12.6.77-1 \[119 MB]

Get:75 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  nsight-compute-2024.3.2 2024.3.2.3-1 \[425 MB]

Get:76 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nsight-compute-12-6 12.6.3-1 \[4056 B]

Get:77 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  nsight-systems-2024.5.1 2024.5.1.113-245134619542v0 \[356 MB]

Get:78 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nsight-systems-12-6 12.6.3-1 \[3352 B]

Get:79 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvml-dev-12-6 12.6.77-1 \[148 kB]

Get:80 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-nvvp-12-6 12.6.80-1 \[115 MB]

Get:81 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-visual-tools-12-6 12.6.3-1 \[2946 B]

Get:82 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  gds-tools-12-6 1.11.1.6-1 \[39.0 MB]

Get:83 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-tools-12-6 12.6.3-1 \[2466 B]

Get:84 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86\_64  cuda-toolkit-12-6 12.6.3-1 \[3324 B]

Fetched 3023 MB in 3min 10s (15.9 MB/s)

Extracting templates from packages: 100%

Preconfiguring packages ...

(Reading database ... 86688 files and directories currently installed.)

Preparing to unpack .../00-ca-certificates\_20260816ubuntu0.24.04.2\_all.deb ...

Unpacking ca-certificates (20260816ubuntu0.24.04.2) over (20240203) ...

Selecting previously unselected package ca-certificates-java.

Preparing to unpack .../01-ca-certificates-java\_20240118ubuntu0.24.04.1\_all.deb ...

Unpacking ca-certificates-java (20240118ubuntu0.24.04.1) ...

Selecting previously unselected package cuda-cccl-12-6.

Preparing to unpack .../02-cuda-cccl-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-cccl-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-cupti-12-6.

Preparing to unpack .../03-cuda-cupti-12-6\_12.6.80-1\_amd64.deb ...

Unpacking cuda-cupti-12-6 (12.6.80-1) ...

Selecting previously unselected package cuda-cupti-dev-12-6.

Preparing to unpack .../04-cuda-cupti-dev-12-6\_12.6.80-1\_amd64.deb ...

Unpacking cuda-cupti-dev-12-6 (12.6.80-1) ...

Selecting previously unselected package cuda-nvdisasm-12-6.

Preparing to unpack .../05-cuda-nvdisasm-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-nvdisasm-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-cuobjdump-12-6.

Preparing to unpack .../06-cuda-cuobjdump-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-cuobjdump-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-gdb-12-6.

Preparing to unpack .../07-cuda-gdb-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-gdb-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-nvprof-12-6.

Preparing to unpack .../08-cuda-nvprof-12-6\_12.6.80-1\_amd64.deb ...

Unpacking cuda-nvprof-12-6 (12.6.80-1) ...

Selecting previously unselected package cuda-nvtx-12-6.

Preparing to unpack .../09-cuda-nvtx-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-nvtx-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-sanitizer-12-6.

Preparing to unpack .../10-cuda-sanitizer-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-sanitizer-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-command-line-tools-12-6.

Preparing to unpack .../11-cuda-command-line-tools-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-command-line-tools-12-6 (12.6.3-1) ...

Selecting previously unselected package cuda-cuxxfilt-12-6.

Preparing to unpack .../12-cuda-cuxxfilt-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-cuxxfilt-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-toolkit-config-common.

Preparing to unpack .../13-cuda-toolkit-config-common\_13.5.37-1\_all.deb ...

Unpacking cuda-toolkit-config-common (13.5.37-1) ...

Selecting previously unselected package cuda-toolkit-12-config-common.

Preparing to unpack .../14-cuda-toolkit-12-config-common\_12.9.79-1\_all.deb ...

Unpacking cuda-toolkit-12-config-common (12.9.79-1) ...

Selecting previously unselected package cuda-toolkit-12-6-config-common.

Preparing to unpack .../15-cuda-toolkit-12-6-config-common\_12.6.77-1\_all.deb ...

Unpacking cuda-toolkit-12-6-config-common (12.6.77-1) ...

Selecting previously unselected package cuda-cudart-12-6.

Preparing to unpack .../16-cuda-cudart-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-cudart-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-driver-dev-12-6.

Preparing to unpack .../17-cuda-driver-dev-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-driver-dev-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-cudart-dev-12-6.

Preparing to unpack .../18-cuda-cudart-dev-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-cudart-dev-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-nvvm-12-6.

Preparing to unpack .../19-cuda-nvvm-12-6\_12.6.85-1\_amd64.deb ...

Unpacking cuda-nvvm-12-6 (12.6.85-1) ...

Selecting previously unselected package cuda-crt-12-6.

Preparing to unpack .../20-cuda-crt-12-6\_12.6.85-1\_amd64.deb ...

Unpacking cuda-crt-12-6 (12.6.85-1) ...

Selecting previously unselected package cuda-nvcc-12-6.

Preparing to unpack .../21-cuda-nvcc-12-6\_12.6.85-1\_amd64.deb ...

Unpacking cuda-nvcc-12-6 (12.6.85-1) ...

Selecting previously unselected package cuda-nvprune-12-6.

Preparing to unpack .../22-cuda-nvprune-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-nvprune-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-compiler-12-6.

Preparing to unpack .../23-cuda-compiler-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-compiler-12-6 (12.6.3-1) ...

Selecting previously unselected package cuda-documentation-12-6.

Preparing to unpack .../24-cuda-documentation-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-documentation-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-nvrtc-12-6.

Preparing to unpack .../25-cuda-nvrtc-12-6\_12.6.85-1\_amd64.deb ...

Unpacking cuda-nvrtc-12-6 (12.6.85-1) ...

Selecting previously unselected package cuda-opencl-12-6.

Preparing to unpack .../26-cuda-opencl-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-opencl-12-6 (12.6.77-1) ...

Selecting previously unselected package libcublas-12-6.

Preparing to unpack .../27-libcublas-12-6\_12.6.4.1-1\_amd64.deb ...

Unpacking libcublas-12-6 (12.6.4.1-1) ...

Selecting previously unselected package libcufft-12-6.

Preparing to unpack .../28-libcufft-12-6\_11.3.0.4-1\_amd64.deb ...

Unpacking libcufft-12-6 (11.3.0.4-1) ...

Selecting previously unselected package libcufile-12-6.

Preparing to unpack .../29-libcufile-12-6\_1.11.1.6-1\_amd64.deb ...

Unpacking libcufile-12-6 (1.11.1.6-1) ...

Selecting previously unselected package libcurand-12-6.

Preparing to unpack .../30-libcurand-12-6\_10.3.7.77-1\_amd64.deb ...

Unpacking libcurand-12-6 (10.3.7.77-1) ...

Selecting previously unselected package libcusolver-12-6.

Preparing to unpack .../31-libcusolver-12-6\_11.7.1.2-1\_amd64.deb ...

Unpacking libcusolver-12-6 (11.7.1.2-1) ...

Selecting previously unselected package libcusparse-12-6.

Preparing to unpack .../32-libcusparse-12-6\_12.5.4.2-1\_amd64.deb ...

Unpacking libcusparse-12-6 (12.5.4.2-1) ...

Selecting previously unselected package libnpp-12-6.

Preparing to unpack .../33-libnpp-12-6\_12.3.1.54-1\_amd64.deb ...

Unpacking libnpp-12-6 (12.3.1.54-1) ...

Selecting previously unselected package libnvjitlink-12-6.

Preparing to unpack .../34-libnvjitlink-12-6\_12.6.85-1\_amd64.deb ...

Unpacking libnvjitlink-12-6 (12.6.85-1) ...

Selecting previously unselected package libnvfatbin-12-6.

Preparing to unpack .../35-libnvfatbin-12-6\_12.6.77-1\_amd64.deb ...

Unpacking libnvfatbin-12-6 (12.6.77-1) ...

Selecting previously unselected package libnvjpeg-12-6.

Preparing to unpack .../36-libnvjpeg-12-6\_12.3.3.54-1\_amd64.deb ...

Unpacking libnvjpeg-12-6 (12.3.3.54-1) ...

Selecting previously unselected package cuda-libraries-12-6.

Preparing to unpack .../37-cuda-libraries-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-libraries-12-6 (12.6.3-1) ...

Selecting previously unselected package cuda-profiler-api-12-6.

Preparing to unpack .../38-cuda-profiler-api-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-profiler-api-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-nvrtc-dev-12-6.

Preparing to unpack .../39-cuda-nvrtc-dev-12-6\_12.6.85-1\_amd64.deb ...

Unpacking cuda-nvrtc-dev-12-6 (12.6.85-1) ...

Selecting previously unselected package cuda-opencl-dev-12-6.

Preparing to unpack .../40-cuda-opencl-dev-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-opencl-dev-12-6 (12.6.77-1) ...

Selecting previously unselected package libcublas-dev-12-6.

Preparing to unpack .../41-libcublas-dev-12-6\_12.6.4.1-1\_amd64.deb ...

Unpacking libcublas-dev-12-6 (12.6.4.1-1) ...

Selecting previously unselected package libcufft-dev-12-6.

Preparing to unpack .../42-libcufft-dev-12-6\_11.3.0.4-1\_amd64.deb ...

Unpacking libcufft-dev-12-6 (11.3.0.4-1) ...

Selecting previously unselected package libcufile-dev-12-6.

Preparing to unpack .../43-libcufile-dev-12-6\_1.11.1.6-1\_amd64.deb ...

Unpacking libcufile-dev-12-6 (1.11.1.6-1) ...

Selecting previously unselected package libcurand-dev-12-6.

Preparing to unpack .../44-libcurand-dev-12-6\_10.3.7.77-1\_amd64.deb ...

Unpacking libcurand-dev-12-6 (10.3.7.77-1) ...

Selecting previously unselected package libcusolver-dev-12-6.

Preparing to unpack .../45-libcusolver-dev-12-6\_11.7.1.2-1\_amd64.deb ...

Unpacking libcusolver-dev-12-6 (11.7.1.2-1) ...

Selecting previously unselected package libcusparse-dev-12-6.

Preparing to unpack .../46-libcusparse-dev-12-6\_12.5.4.2-1\_amd64.deb ...

Unpacking libcusparse-dev-12-6 (12.5.4.2-1) ...

Selecting previously unselected package libnpp-dev-12-6.

Preparing to unpack .../47-libnpp-dev-12-6\_12.3.1.54-1\_amd64.deb ...

Unpacking libnpp-dev-12-6 (12.3.1.54-1) ...

Selecting previously unselected package libnvjitlink-dev-12-6.

Preparing to unpack .../48-libnvjitlink-dev-12-6\_12.6.85-1\_amd64.deb ...

Unpacking libnvjitlink-dev-12-6 (12.6.85-1) ...

Selecting previously unselected package libnvfatbin-dev-12-6.

Preparing to unpack .../49-libnvfatbin-dev-12-6\_12.6.77-1\_amd64.deb ...

Unpacking libnvfatbin-dev-12-6 (12.6.77-1) ...

Selecting previously unselected package libnvjpeg-dev-12-6.

Preparing to unpack .../50-libnvjpeg-dev-12-6\_12.3.3.54-1\_amd64.deb ...

Unpacking libnvjpeg-dev-12-6 (12.3.3.54-1) ...

Selecting previously unselected package cuda-libraries-dev-12-6.

Preparing to unpack .../51-cuda-libraries-dev-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-libraries-dev-12-6 (12.6.3-1) ...

Selecting previously unselected package java-common.

Preparing to unpack .../52-java-common\_0.75+exp1\_all.deb ...

Unpacking java-common (0.75+exp1) ...

Selecting previously unselected package libnspr4:amd64.

Preparing to unpack .../53-libnspr4\_2%3a4.35-1.1build1\_amd64.deb ...

Unpacking libnspr4:amd64 (2:4.35-1.1build1) ...

Selecting previously unselected package libnss3:amd64.

Preparing to unpack .../54-libnss3\_2%3a3.98-1ubuntu0.3\_amd64.deb ...

Unpacking libnss3:amd64 (2:3.98-1ubuntu0.3) ...

Selecting previously unselected package libpcsclite1:amd64.

Preparing to unpack .../55-libpcsclite1\_2.0.3-1build1\_amd64.deb ...

Unpacking libpcsclite1:amd64 (2.0.3-1build1) ...

Selecting previously unselected package openjdk-21-jre-headless:amd64.

Preparing to unpack .../56-openjdk-21-jre-headless\_21.0.12.1+1-1\~24.04.4\_amd64.deb ...

Unpacking openjdk-21-jre-headless:amd64 (21.0.12.1+1-1\~24.04.4) ...

Selecting previously unselected package default-jre-headless.

Preparing to unpack .../57-default-jre-headless\_2%3a1.21-75+exp1\_amd64.deb ...

Unpacking default-jre-headless (2:1.21-75+exp1) ...

Selecting previously unselected package libgif7:amd64.

Preparing to unpack .../58-libgif7\_5.2.2-1ubuntu1.2\_amd64.deb ...

Unpacking libgif7:amd64 (5.2.2-1ubuntu1.2) ...

Selecting previously unselected package openjdk-21-jre:amd64.

Preparing to unpack .../59-openjdk-21-jre\_21.0.12.1+1-1\~24.04.4\_amd64.deb ...

Unpacking openjdk-21-jre:amd64 (21.0.12.1+1-1\~24.04.4) ...

Selecting previously unselected package default-jre.

Preparing to unpack .../60-default-jre\_2%3a1.21-75+exp1\_amd64.deb ...

Unpacking default-jre (2:1.21-75+exp1) ...

Selecting previously unselected package cuda-nsight-12-6.

Preparing to unpack .../61-cuda-nsight-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-nsight-12-6 (12.6.77-1) ...

Selecting previously unselected package nsight-compute-2024.3.2.

Preparing to unpack .../62-nsight-compute-2024.3.2\_2024.3.2.3-1\_amd64.deb ...

Unpacking nsight-compute-2024.3.2 (2024.3.2.3-1) ...

Selecting previously unselected package cuda-nsight-compute-12-6.

Preparing to unpack .../63-cuda-nsight-compute-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-nsight-compute-12-6 (12.6.3-1) ...

Selecting previously unselected package libxcb-xinerama0:amd64.

Preparing to unpack .../64-libxcb-xinerama0\_1.15-1ubuntu2\_amd64.deb ...

Unpacking libxcb-xinerama0:amd64 (1.15-1ubuntu2) ...

Selecting previously unselected package libxcb-icccm4:amd64.

Preparing to unpack .../65-libxcb-icccm4\_0.4.1-1.1build3\_amd64.deb ...

Unpacking libxcb-icccm4:amd64 (0.4.1-1.1build3) ...

Selecting previously unselected package libxcb-util1:amd64.

Preparing to unpack .../66-libxcb-util1\_0.4.0-1build3\_amd64.deb ...

Unpacking libxcb-util1:amd64 (0.4.0-1build3) ...

Selecting previously unselected package libxcb-image0:amd64.

Preparing to unpack .../67-libxcb-image0\_0.4.0-2build1\_amd64.deb ...

Unpacking libxcb-image0:amd64 (0.4.0-2build1) ...

Selecting previously unselected package libxcb-keysyms1:amd64.

Preparing to unpack .../68-libxcb-keysyms1\_0.4.0-1build4\_amd64.deb ...

Unpacking libxcb-keysyms1:amd64 (0.4.0-1build4) ...

Selecting previously unselected package libxcb-render-util0:amd64.

Preparing to unpack .../69-libxcb-render-util0\_0.3.9-1build4\_amd64.deb ...

Unpacking libxcb-render-util0:amd64 (0.3.9-1build4) ...

Selecting previously unselected package libxcb-xkb1:amd64.

Preparing to unpack .../70-libxcb-xkb1\_1.15-1ubuntu2\_amd64.deb ...

Unpacking libxcb-xkb1:amd64 (1.15-1ubuntu2) ...

Selecting previously unselected package libxkbcommon-x11-0:amd64.

Preparing to unpack .../71-libxkbcommon-x11-0\_1.6.0-1build1\_amd64.deb ...

Unpacking libxkbcommon-x11-0:amd64 (1.6.0-1build1) ...

Selecting previously unselected package libxcb-xinput0:amd64.

Preparing to unpack .../72-libxcb-xinput0\_1.15-1ubuntu2\_amd64.deb ...

Unpacking libxcb-xinput0:amd64 (1.15-1ubuntu2) ...

Selecting previously unselected package libxcb-cursor0:amd64.

Preparing to unpack .../73-libxcb-cursor0\_0.1.4-1build1\_amd64.deb ...

Unpacking libxcb-cursor0:amd64 (0.1.4-1build1) ...

Selecting previously unselected package nsight-systems-2024.5.1.

Preparing to unpack .../74-nsight-systems-2024.5.1\_2024.5.1.113-245134619542v0\_amd64.deb ...

Unpacking nsight-systems-2024.5.1 (2024.5.1.113-245134619542v0) ...

Selecting previously unselected package cuda-nsight-systems-12-6.

Preparing to unpack .../75-cuda-nsight-systems-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-nsight-systems-12-6 (12.6.3-1) ...

Selecting previously unselected package cuda-nvml-dev-12-6.

Preparing to unpack .../76-cuda-nvml-dev-12-6\_12.6.77-1\_amd64.deb ...

Unpacking cuda-nvml-dev-12-6 (12.6.77-1) ...

Selecting previously unselected package cuda-nvvp-12-6.

Preparing to unpack .../77-cuda-nvvp-12-6\_12.6.80-1\_amd64.deb ...

Unpacking cuda-nvvp-12-6 (12.6.80-1) ...

Selecting previously unselected package cuda-visual-tools-12-6.

Preparing to unpack .../78-cuda-visual-tools-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-visual-tools-12-6 (12.6.3-1) ...

Selecting previously unselected package gds-tools-12-6.

Preparing to unpack .../79-gds-tools-12-6\_1.11.1.6-1\_amd64.deb ...

Unpacking gds-tools-12-6 (1.11.1.6-1) ...

Selecting previously unselected package cuda-tools-12-6.

Preparing to unpack .../80-cuda-tools-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-tools-12-6 (12.6.3-1) ...

Selecting previously unselected package cuda-toolkit-12-6.

Preparing to unpack .../81-cuda-toolkit-12-6\_12.6.3-1\_amd64.deb ...

Unpacking cuda-toolkit-12-6 (12.6.3-1) ...

Selecting previously unselected package fonts-dejavu-extra.

Preparing to unpack .../82-fonts-dejavu-extra\_2.37-8\_all.deb ...

Unpacking fonts-dejavu-extra (2.37-8) ...

Selecting previously unselected package libatk-wrapper-java.

Preparing to unpack .../83-libatk-wrapper-java\_0.40.0-3build2\_all.deb ...

Unpacking libatk-wrapper-java (0.40.0-3build2) ...

Selecting previously unselected package libatk-wrapper-java-jni:amd64.

Preparing to unpack .../84-libatk-wrapper-java-jni\_0.40.0-3build2\_amd64.deb ...

Unpacking libatk-wrapper-java-jni:amd64 (0.40.0-3build2) ...

Setting up cuda-cccl-12-6 (12.6.77-1) ...

Setting up cuda-toolkit-config-common (13.5.37-1) ...

Setting up gds-tools-12-6 (1.11.1.6-1) ...

Setting up cuda-documentation-12-6 (12.6.77-1) ...

Setting up java-common (0.75+exp1) ...

Setting up libxcb-xinput0:amd64 (1.15-1ubuntu2) ...

Setting up cuda-nvml-dev-12-6 (12.6.77-1) ...

Setting up cuda-profiler-api-12-6 (12.6.77-1) ...

Setting up libxcb-keysyms1:amd64 (0.4.0-1build4) ...

Setting up libxcb-render-util0:amd64 (0.3.9-1build4) ...

Setting up nsight-compute-2024.3.2 (2024.3.2.3-1) ...

Setting up cuda-nvvm-12-6 (12.6.85-1) ...

Setting up libxcb-icccm4:amd64 (0.4.1-1.1build3) ...

Setting up cuda-nvtx-12-6 (12.6.77-1) ...

Setting up libxcb-util1:amd64 (0.4.0-1build3) ...

Setting up libxcb-xkb1:amd64 (1.15-1ubuntu2) ...

Setting up libxcb-image0:amd64 (0.4.0-2build1) ...

Setting up cuda-cuxxfilt-12-6 (12.6.77-1) ...

Setting up ca-certificates (20260816ubuntu0.24.04.2) ...

Updating certificates in /etc/ssl/certs...

rehash: warning: skipping ca-certificates.crt,it does not contain exactly one certificate or CRL

17 added, 43 removed; done.

Running hooks in /etc/ca-certificates/update.d...

done.

Setting up libxcb-xinerama0:amd64 (1.15-1ubuntu2) ...

Setting up cuda-nvdisasm-12-6 (12.6.77-1) ...

Setting up libnspr4:amd64 (2:4.35-1.1build1) ...

Setting up libxcb-cursor0:amd64 (0.1.4-1build1) ...

Setting up cuda-nvprune-12-6 (12.6.77-1) ...

Setting up libxkbcommon-x11-0:amd64 (1.6.0-1build1) ...

Setting up cuda-driver-dev-12-6 (12.6.77-1) ...

Setting up cuda-nsight-compute-12-6 (12.6.3-1) ...

Setting up libpcsclite1:amd64 (2.0.3-1build1) ...

Setting up libgif7:amd64 (5.2.2-1ubuntu1.2) ...

Setting up fonts-dejavu-extra (2.37-8) ...

Setting up cuda-toolkit-12-6-config-common (12.6.77-1) ...

Setting alternatives

update-alternatives: using /usr/local/cuda-12.6 to provide /usr/local/cuda (cuda) in auto mode

update-alternatives: using /usr/local/cuda-12.6 to provide /usr/local/cuda-12 (cuda-12) in auto mode

Setting up cuda-cuobjdump-12-6 (12.6.77-1) ...

Setting up cuda-nvrtc-12-6 (12.6.85-1) ...

Setting up cuda-sanitizer-12-6 (12.6.77-1) ...

Setting up libatk-wrapper-java (0.40.0-3build2) ...

Setting up ca-certificates-java (20240118ubuntu0.24.04.1) ...

No JRE found. Skipping Java certificates setup.

Setting up cuda-cupti-12-6 (12.6.80-1) ...

Setting up cuda-nvprof-12-6 (12.6.80-1) ...

Setting up cuda-toolkit-12-config-common (12.9.79-1) ...

Setting up libcusolver-12-6 (11.7.1.2-1) ...

Setting up libnvjitlink-12-6 (12.6.85-1) ...

Setting up libcurand-12-6 (10.3.7.77-1) ...

Setting up libcufft-12-6 (11.3.0.4-1) ...

Setting up libcufft-dev-12-6 (11.3.0.4-1) ...

Setting up libnpp-12-6 (12.3.1.54-1) ...

Setting up libnvjitlink-dev-12-6 (12.6.85-1) ...

Setting up libcusparse-12-6 (12.5.4.2-1) ...

Setting up cuda-cupti-dev-12-6 (12.6.80-1) ...

Setting up libnvfatbin-12-6 (12.6.77-1) ...

Setting up libcurand-dev-12-6 (10.3.7.77-1) ...

Setting up libnss3:amd64 (2:3.98-1ubuntu0.3) ...

Setting up libatk-wrapper-java-jni:amd64 (0.40.0-3build2) ...

Setting up libnpp-dev-12-6 (12.3.1.54-1) ...

Setting up libcublas-12-6 (12.6.4.1-1) ...

Setting up libcublas-dev-12-6 (12.6.4.1-1) ...

Setting up cuda-cudart-12-6 (12.6.77-1) ...

Setting up cuda-gdb-12-6 (12.6.77-1) ...

Setting up libnvjpeg-12-6 (12.3.3.54-1) ...

Setting up libcufile-12-6 (1.11.1.6-1) ...

Setting alternatives

update-alternatives: using /usr/local/cuda-12.6/gds/cufile.json to provide /etc/cufile.json (cufile.json) in auto mode

Setting up cuda-opencl-12-6 (12.6.77-1) ...

Setting up libcusparse-dev-12-6 (12.5.4.2-1) ...

Setting up cuda-libraries-12-6 (12.6.3-1) ...

Setting up cuda-nvrtc-dev-12-6 (12.6.85-1) ...

Setting up libcusolver-dev-12-6 (11.7.1.2-1) ...

Setting up cuda-command-line-tools-12-6 (12.6.3-1) ...

Setting up cuda-opencl-dev-12-6 (12.6.77-1) ...

Setting up openjdk-21-jre-headless:amd64 (21.0.12.1+1-1\~24.04.4) ...

update-alternatives: using /usr/lib/jvm/java-21-openjdk-amd64/bin/java to provide /usr/bin/java (java) in auto mode

update-alternatives: using /usr/lib/jvm/java-21-openjdk-amd64/bin/jpackage to provide /usr/bin/jpackage (jpackage) in auto mode

update-alternatives: using /usr/lib/jvm/java-21-openjdk-amd64/bin/keytool to provide /usr/bin/keytool (keytool) in auto mode

update-alternatives: using /usr/lib/jvm/java-21-openjdk-amd64/bin/rmiregistry to provide /usr/bin/rmiregistry (rmiregistry) in auto mode

update-alternatives: using /usr/lib/jvm/java-21-openjdk-amd64/lib/jexec to provide /usr/bin/jexec (jexec) in auto mode

Setting up nsight-systems-2024.5.1 (2024.5.1.113-245134619542v0) ...

update-alternatives: using /opt/nvidia/nsight-systems/2024.5.1/target-linux-x64/nsys to provide /usr/local/bin/nsys (nsys) in auto mode

update-alternatives: using /opt/nvidia/nsight-systems/2024.5.1/host-linux-x64/nsys-ui to provide /usr/local/bin/nsys-ui (nsys-ui) in auto mode

Setting up libnvfatbin-dev-12-6 (12.6.77-1) ...

Setting up libnvjpeg-dev-12-6 (12.3.3.54-1) ...

Setting up libcufile-dev-12-6 (1.11.1.6-1) ...

Setting up cuda-cudart-dev-12-6 (12.6.77-1) ...

Setting up cuda-libraries-dev-12-6 (12.6.3-1) ...

Setting up cuda-nsight-systems-12-6 (12.6.3-1) ...

Setting up cuda-crt-12-6 (12.6.85-1) ...

Setting up cuda-nvcc-12-6 (12.6.85-1) ...

Setting up cuda-compiler-12-6 (12.6.3-1) ...

Processing triggers for fontconfig (2.15.0-1.1ubuntu2) ...

Processing triggers for hicolor-icon-theme (0.17-2) ...

Processing triggers for libc-bin (2.39-0ubuntu8.7) ...

Processing triggers for man-db (2.12.0-4build2) ...

Processing triggers for ca-certificates-java (20240118ubuntu0.24.04.1) ...

Adding debian:ACCVRAIZ1.pem

Adding debian:AC\_RAIZ\_FNMT-RCM.pem

Adding debian:AC\_RAIZ\_FNMT-RCM\_SERVIDORES\_SEGUROS.pem

Adding debian:ANF\_Secure\_Server\_Root\_CA.pem

Adding debian:Actalis\_Authentication\_Root\_CA.pem

Adding debian:Amazon\_Root\_CA\_1.pem

Adding debian:Amazon\_Root\_CA\_2.pem

Adding debian:Amazon\_Root\_CA\_3.pem

Adding debian:Amazon\_Root\_CA\_4.pem

Adding debian:Atos\_TrustedRoot\_Root\_CA\_ECC\_TLS\_2021.pem

Adding debian:Atos\_TrustedRoot\_Root\_CA\_RSA\_TLS\_2021.pem

Adding debian:Autoridad\_de\_Certificacion\_Firmaprofesional\_CIF\_A62634068.pem

Adding debian:BJCA\_Global\_Root\_CA1.pem

Adding debian:BJCA\_Global\_Root\_CA2.pem

Adding debian:Buypass\_Class\_2\_Root\_CA.pem

Adding debian:Buypass\_Class\_3\_Root\_CA.pem

Adding debian:CA\_Disig\_Root\_R2.pem

Adding debian:CFCA\_EV\_ROOT.pem

Adding debian:COMODO\_ECC\_Certification\_Authority.pem

Adding debian:COMODO\_RSA\_Certification\_Authority.pem

Adding debian:Certainly\_Root\_E1.pem

Adding debian:Certainly\_Root\_R1.pem

Adding debian:Certigna\_Root\_CA.pem

Adding debian:Certum\_EC-384\_CA.pem

Adding debian:Certum\_Trusted\_Network\_CA.pem

Adding debian:Certum\_Trusted\_Network\_CA\_2.pem

Adding debian:Certum\_Trusted\_Root\_CA.pem

Adding debian:D-TRUST\_BR\_Root\_CA\_1\_2020.pem

Adding debian:D-TRUST\_BR\_Root\_CA\_2\_2023.pem

Adding debian:D-TRUST\_EV\_Root\_CA\_1\_2020.pem

Adding debian:D-TRUST\_EV\_Root\_CA\_2\_2023.pem

Adding debian:D-TRUST\_Root\_Class\_3\_CA\_2\_2009.pem

Adding debian:D-TRUST\_Root\_Class\_3\_CA\_2\_EV\_2009.pem

Adding debian:DigiCert\_Assured\_ID\_Root\_G2.pem

Adding debian:DigiCert\_Assured\_ID\_Root\_G3.pem

Adding debian:DigiCert\_Global\_Root\_G2.pem

Adding debian:DigiCert\_Global\_Root\_G3.pem

Adding debian:DigiCert\_TLS\_ECC\_P384\_Root\_G5.pem

Adding debian:DigiCert\_TLS\_RSA4096\_Root\_G5.pem

Adding debian:DigiCert\_Trusted\_Root\_G4.pem

Adding debian:GDCA\_TrustAUTH\_R5\_ROOT.pem

Adding debian:GTS\_Root\_R1.pem

Adding debian:GTS\_Root\_R3.pem

Adding debian:GTS\_Root\_R4.pem

Adding debian:GlobalSign\_ECC\_Root\_CA\_-\_R4.pem

Adding debian:GlobalSign\_ECC\_Root\_CA\_-\_R5.pem

Adding debian:GlobalSign\_Root\_CA\_-\_R3.pem

Adding debian:GlobalSign\_Root\_CA\_-\_R6.pem

Adding debian:GlobalSign\_Root\_E46.pem

Adding debian:GlobalSign\_Root\_R46.pem

Adding debian:Go\_Daddy\_Root\_Certificate\_Authority\_-\_G2.pem

Adding debian:HARICA\_TLS\_ECC\_Root\_CA\_2021.pem

Adding debian:HARICA\_TLS\_RSA\_Root\_CA\_2021.pem

Adding debian:Hellenic\_Academic\_and\_Research\_Institutions\_ECC\_RootCA\_2015.pem

Adding debian:Hellenic\_Academic\_and\_Research\_Institutions\_RootCA\_2015.pem

Adding debian:HiPKI\_Root\_CA\_-\_G1.pem

Adding debian:Hongkong\_Post\_Root\_CA\_3.pem

Adding debian:ISRG\_Root\_X1.pem

Adding debian:ISRG\_Root\_X2.pem

Adding debian:IdenTrust\_Commercial\_Root\_CA\_1.pem

Adding debian:IdenTrust\_Public\_Sector\_Root\_CA\_1.pem

Adding debian:Izenpe.com.pem

Adding debian:Microsec\_e-Szigno\_Root\_CA\_2009.pem

Adding debian:Microsoft\_ECC\_Root\_Certificate\_Authority\_2017.pem

Adding debian:Microsoft\_RSA\_Root\_Certificate\_Authority\_2017.pem

Adding debian:NAVER\_Global\_Root\_Certification\_Authority.pem

Adding debian:NetLock\_Arany\_=Class\_Gold=\_Főtanúsítvány.pem

Adding debian:OISTE\_Server\_Root\_ECC\_G1.pem

Adding debian:OISTE\_Server\_Root\_RSA\_G1.pem

Adding debian:OISTE\_WISeKey\_Global\_Root\_GB\_CA.pem

Adding debian:OISTE\_WISeKey\_Global\_Root\_GC\_CA.pem

Adding debian:QuoVadis\_Root\_CA\_1\_G3.pem

Adding debian:QuoVadis\_Root\_CA\_2\_G3.pem

Adding debian:QuoVadis\_Root\_CA\_3\_G3.pem

Adding debian:SECOM\_TLS\_ECC\_Root\_CA\_2024.pem

Adding debian:SECOM\_TLS\_RSA\_Root\_CA\_2024.pem

Adding debian:SSL.com\_EV\_Root\_Certification\_Authority\_ECC.pem

Adding debian:SSL.com\_EV\_Root\_Certification\_Authority\_RSA\_R2.pem

Adding debian:SSL.com\_Root\_Certification\_Authority\_ECC.pem

Adding debian:SSL.com\_Root\_Certification\_Authority\_RSA.pem

Adding debian:SSL.com\_TLS\_ECC\_Root\_CA\_2022.pem

Adding debian:SSL.com\_TLS\_RSA\_Root\_CA\_2022.pem

Adding debian:SZAFIR\_ROOT\_CA2.pem

Adding debian:Sectigo\_Public\_Server\_Authentication\_Root\_E46.pem

Adding debian:Sectigo\_Public\_Server\_Authentication\_Root\_R46.pem

Adding debian:SecureSign\_Root\_CA14.pem

Adding debian:SecureSign\_Root\_CA15.pem

Adding debian:Security\_Communication\_ECC\_RootCA1.pem

Adding debian:Security\_Communication\_RootCA2.pem

Adding debian:Starfield\_Root\_Certificate\_Authority\_-\_G2.pem

Adding debian:Starfield\_Services\_Root\_Certificate\_Authority\_-\_G2.pem

Adding debian:SwissSign\_RSA\_TLS\_Root\_CA\_2022\_-\_1.pem

Adding debian:T-TeleSec\_GlobalRoot\_Class\_2.pem

Adding debian:T-TeleSec\_GlobalRoot\_Class\_3.pem

Adding debian:TUBITAK\_Kamu\_SM\_SSL\_Kok\_Sertifikasi\_-\_Surum\_1.pem

Adding debian:TWCA\_CYBER\_Root\_CA.pem

Adding debian:TWCA\_Global\_Root\_CA.pem

Adding debian:TWCA\_Root\_Certification\_Authority.pem

Adding debian:Telekom\_Security\_TLS\_ECC\_Root\_2020.pem

Adding debian:Telekom\_Security\_TLS\_RSA\_Root\_2023.pem

Adding debian:Telia\_EC\_TLS\_Root\_CA\_v3.pem

Adding debian:Telia\_RSA\_TLS\_Root\_CA\_v3.pem

Adding debian:Telia\_Root\_CA\_v2.pem

Adding debian:TrustAsia\_Global\_Root\_CA\_G3.pem

Adding debian:TrustAsia\_Global\_Root\_CA\_G4.pem

Adding debian:TrustAsia\_TLS\_ECC\_Root\_CA.pem

Adding debian:TrustAsia\_TLS\_RSA\_Root\_CA.pem

Adding debian:TunTrust\_Root\_CA.pem

Adding debian:UCA\_Extended\_Validation\_Root.pem

Adding debian:UCA\_Global\_G2\_Root.pem

Adding debian:USERTrust\_ECC\_Certification\_Authority.pem

Adding debian:USERTrust\_RSA\_Certification\_Authority.pem

Adding debian:certSIGN\_Root\_CA\_G2.pem

Adding debian:e-Szigno\_Root\_CA\_2017.pem

Adding debian:e-Szigno\_TLS\_Root\_CA\_2023.pem

Adding debian:emSign\_ECC\_Root\_CA\_-\_C3.pem

Adding debian:emSign\_Root\_CA\_-\_C1.pem

Adding debian:emSign\_Root\_CA\_-\_G1.pem

Adding debian:vTrus\_ECC\_Root\_CA.pem

Adding debian:vTrus\_Root\_CA.pem

done.

Setting up openjdk-21-jre:amd64 (21.0.12.1+1-1\~24.04.4) ...

Setting up default-jre-headless (2:1.21-75+exp1) ...

Setting up default-jre (2:1.21-75+exp1) ...

Setting up cuda-nvvp-12-6 (12.6.80-1) ...

Setting up cuda-nsight-12-6 (12.6.77-1) ...

Setting up cuda-visual-tools-12-6 (12.6.3-1) ...

Setting up cuda-tools-12-6 (12.6.3-1) ...

Setting up cuda-toolkit-12-6 (12.6.3-1) ...

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ export CUDA\_HOME=/usr/local/cuda-12.6

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ export PATH=$CUDA\_HOME/bin:$PATH

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ nvcc --version

nvcc: NVIDIA (R) Cuda compiler driver

Copyright (c) 2005-2024 NVIDIA Corporation

Built on Tue\_Oct\_29\_23:50:19\_PDT\_2024

Cuda compilation tools, release 12.6, V12.6.85

Build cuda\_12.6.r12.6/compiler.35059454\_0

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ pip uninstall -y adam-atan2

Found existing installation: adam\_atan2 0.0.3

Uninstalling adam\_atan2-0.0.3:

&#x20; Successfully uninstalled adam\_atan2-0.0.3

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code/TinyRecursiveModels$ cd /tmp

(TRM) mathi@Schneller-Hobel:/tmp$ git clone https://github.com/imoneoi/adam-atan2.git

Cloning into 'adam-atan2'...

remote: Enumerating objects: 113, done.

remote: Counting objects: 100% (113/113), done.

remote: Compressing objects: 100% (56/56), done.

remote: Total 113 (delta 55), reused 113 (delta 55), pack-reused 0 (from 0)

Receiving objects: 100% (113/113), 25.72 KiB | 3.67 MiB/s, done.

Resolving deltas: 100% (55/55), done.

(TRM) mathi@Schneller-Hobel:/tmp$ cd adam-atan2

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ sed -i 's/NVIDIA\_SUPPORTED\_ARCHS = {"80", "86", "89", "90"}/NVIDIA\_SUPPORTED\_ARCHS = {"75"}/' setup.py

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ export CUDA\_HOME=/usr/local/cuda-12.6

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ MAX\_JOBS=1 pip install --no-cache-dir --no-build-isolation -v .

Using pip 26.3 from /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/pip (python 3.10)

Processing ./.

&#x20; Running command Preparing metadata (pyproject.toml)

&#x20; running dist\_info

&#x20; creating /tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info

&#x20; writing /tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info/PKG-INFO

&#x20; writing dependency\_links to /tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info/dependency\_links.txt

&#x20; writing top-level names to /tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info/top\_level.txt

&#x20; writing manifest file '/tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info/SOURCES.txt'

&#x20; adding license file 'LICENSE'

&#x20; writing manifest file '/tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2.egg-info/SOURCES.txt'

&#x20; creating '/tmp/pip-modern-metadata-ifo8tz\_u/adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info'

&#x20; Preparing metadata (pyproject.toml) ... done

&#x20; /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/setuptools/dist.py:759: BuildBackendWarning: License classifiers are deprecated.

&#x20; !!



&#x20;         \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;         Please consider removing the following classifiers in favor of a SPDX license expression:



&#x20;         License :: OSI Approved :: Apache Software License



&#x20;         See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.

&#x20;         \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



&#x20; !!

&#x20;   self.\_finalize\_license\_expression()

Building wheels for collected packages: adam\_atan2

&#x20; Running command Building wheel for adam\_atan2 (pyproject.toml)

&#x20; running bdist\_wheel

&#x20; running build

&#x20; running build\_py

&#x20; creating build/lib.linux-x86\_64-cpython-310/adam\_atan2

&#x20; copying adam\_atan2/\_\_init\_\_.py -> build/lib.linux-x86\_64-cpython-310/adam\_atan2

&#x20; copying adam\_atan2/adam\_atan2.py -> build/lib.linux-x86\_64-cpython-310/adam\_atan2

&#x20; copying adam\_atan2/adam\_atan2\_test.py -> build/lib.linux-x86\_64-cpython-310/adam\_atan2

&#x20; running build\_ext

&#x20; building 'adam\_atan2\_backend' extension

&#x20; creating /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc

&#x20; Emitting ninja build file /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/build.ninja...

&#x20; Compiling objects...

&#x20; Using envvar MAX\_JOBS (1) as the number of workers...

&#x20; \[1/2] /usr/local/cuda-12.6/bin/nvcc --generate-dependencies-with-compile --dependency-output /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/adam\_atan2.o.d -I/tmp/adam-atan2/csrc -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/TH -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/THC -I/usr/local/cuda-12.6/include -I/home/mathi/miniconda3/envs/TRM/include/python3.10 -c -c /tmp/adam-atan2/csrc/adam\_atan2.cu -o /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/adam\_atan2.o -D\_\_CUDA\_NO\_HALF\_OPERATORS\_\_ -D\_\_CUDA\_NO\_HALF\_CONVERSIONS\_\_ -D\_\_CUDA\_NO\_BFLOAT16\_CONVERSIONS\_\_ -D\_\_CUDA\_NO\_HALF2\_OPERATORS\_\_ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 --expt-extended-lambda --generate-code=arch=compute\_75,code=sm\_75 -DTORCH\_API\_INCLUDE\_EXTENSION\_H '-DPYBIND11\_COMPILER\_TYPE="\_gcc"' '-DPYBIND11\_STDLIB="\_libstdcpp"' '-DPYBIND11\_BUILD\_ABI="\_cxxabi1016"' -DTORCH\_EXTENSION\_NAME=adam\_atan2\_backend -D\_GLIBCXX\_USE\_CXX11\_ABI=1

&#x20; \[2/2] /usr/local/cuda-12.6/bin/nvcc --generate-dependencies-with-compile --dependency-output /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/ops.o.d -I/tmp/adam-atan2/csrc -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/torch/csrc/api/include -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/TH -I/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/include/THC -I/usr/local/cuda-12.6/include -I/home/mathi/miniconda3/envs/TRM/include/python3.10 -c -c /tmp/adam-atan2/csrc/ops.cu -o /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/ops.o -D\_\_CUDA\_NO\_HALF\_OPERATORS\_\_ -D\_\_CUDA\_NO\_HALF\_CONVERSIONS\_\_ -D\_\_CUDA\_NO\_BFLOAT16\_CONVERSIONS\_\_ -D\_\_CUDA\_NO\_HALF2\_OPERATORS\_\_ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O2 -std=c++17 --expt-extended-lambda --generate-code=arch=compute\_75,code=sm\_75 -DTORCH\_API\_INCLUDE\_EXTENSION\_H '-DPYBIND11\_COMPILER\_TYPE="\_gcc"' '-DPYBIND11\_STDLIB="\_libstdcpp"' '-DPYBIND11\_BUILD\_ABI="\_cxxabi1016"' -DTORCH\_EXTENSION\_NAME=adam\_atan2\_backend -D\_GLIBCXX\_USE\_CXX11\_ABI=1

&#x20; g++ -pthread -B /home/mathi/miniconda3/envs/TRM/compiler\_compat -Wno-unused-result -Wsign-compare -DNDEBUG -fwrapv -O2 -Wall -fPIC -O2 -isystem /home/mathi/miniconda3/envs/TRM/include -fPIC -O2 -isystem /home/mathi/miniconda3/envs/TRM/include -shared /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/adam\_atan2.o /tmp/adam-atan2/build/temp.linux-x86\_64-cpython-310/csrc/ops.o -L/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/lib -L/usr/local/cuda-12.6/lib64 -lc10 -ltorch -ltorch\_cpu -ltorch\_python -lcudart -lc10\_cuda -ltorch\_cuda -o build/lib.linux-x86\_64-cpython-310/adam\_atan2\_backend.cpython-310-x86\_64-linux-gnu.so

&#x20; installing to build/bdist.linux-x86\_64/wheel

&#x20; running install

&#x20; running install\_lib

&#x20; creating build/bdist.linux-x86\_64/wheel

&#x20; copying build/lib.linux-x86\_64-cpython-310/adam\_atan2\_backend.cpython-310-x86\_64-linux-gnu.so -> build/bdist.linux-x86\_64/wheel/.

&#x20; creating build/bdist.linux-x86\_64/wheel/adam\_atan2

&#x20; copying build/lib.linux-x86\_64-cpython-310/adam\_atan2/\_\_init\_\_.py -> build/bdist.linux-x86\_64/wheel/./adam\_atan2

&#x20; copying build/lib.linux-x86\_64-cpython-310/adam\_atan2/adam\_atan2.py -> build/bdist.linux-x86\_64/wheel/./adam\_atan2

&#x20; copying build/lib.linux-x86\_64-cpython-310/adam\_atan2/adam\_atan2\_test.py -> build/bdist.linux-x86\_64/wheel/./adam\_atan2

&#x20; running install\_egg\_info

&#x20; running egg\_info

&#x20; creating adam\_atan2.egg-info

&#x20; writing adam\_atan2.egg-info/PKG-INFO

&#x20; writing dependency\_links to adam\_atan2.egg-info/dependency\_links.txt

&#x20; writing top-level names to adam\_atan2.egg-info/top\_level.txt

&#x20; writing manifest file 'adam\_atan2.egg-info/SOURCES.txt'

&#x20; adding license file 'LICENSE'

&#x20; writing manifest file 'adam\_atan2.egg-info/SOURCES.txt'

&#x20; Copying adam\_atan2.egg-info to build/bdist.linux-x86\_64/wheel/./adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109-py3.10.egg-info

&#x20; running install\_scripts

&#x20; creating build/bdist.linux-x86\_64/wheel/adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/WHEEL

&#x20; creating '/tmp/pip-ephem-wheel-cache-5s5jg1mf/wheels/f7/b2/39/e4132d3bb344b31496e9c72f9aaf3280d3419911d230d2864e/tmprxisdbvw/.tmp-l5qgggax/adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109-cp310-cp310-linux\_x86\_64.whl' and adding 'build/bdist.linux-x86\_64/wheel' to it

&#x20; adding 'adam\_atan2\_backend.cpython-310-x86\_64-linux-gnu.so'

&#x20; adding 'adam\_atan2/\_\_init\_\_.py'

&#x20; adding 'adam\_atan2/adam\_atan2.py'

&#x20; adding 'adam\_atan2/adam\_atan2\_test.py'

&#x20; adding 'adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/licenses/LICENSE'

&#x20; adding 'adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/METADATA'

&#x20; adding 'adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/WHEEL'

&#x20; adding 'adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/top\_level.txt'

&#x20; adding 'adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109.dist-info/RECORD'

&#x20; removing build/bdist.linux-x86\_64/wheel

&#x20; Building wheel for adam\_atan2 (pyproject.toml) ... done

&#x20; /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/setuptools/dist.py:759: BuildBackendWarning: License classifiers are deprecated.

&#x20; !!



&#x20;         \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;         Please consider removing the following classifiers in favor of a SPDX license expression:



&#x20;         License :: OSI Approved :: Apache Software License



&#x20;         See https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#license for details.

&#x20;         \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



&#x20; !!

&#x20;   self.\_finalize\_license\_expression()

&#x20; /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/torch/utils/cpp\_extension.py:458: BuildBackendWarning: There are no g++ version bounds defined for CUDA version 12.6

&#x20;   warnings.warn(f'There are no {compiler\_name} version bounds defined for CUDA version {cuda\_str\_version}')

&#x20; Created wheel for adam\_atan2: filename=adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109-cp310-cp310-linux\_x86\_64.whl size=117733 sha256=703a991af5742a891afe9c30dfd0f4877af26aa1e051d991e2f6f8552b2d2798

&#x20; Stored in directory: /tmp/pip-ephem-wheel-cache-5s5jg1mf/wheels/f7/b2/39/e4132d3bb344b31496e9c72f9aaf3280d3419911d230d2864e

Successfully built adam\_atan2

Installing collected packages: adam\_atan2

Successfully installed adam\_atan2-0.0.4.dev0+g42a1aeb38.d20261109

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ python -c "import adam\_atan2; print('Import erfolgreich!')"

\-bash: !': event not found

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ python -c "import adam\_atan2; print('Import erfolgreich!')"

\-bash: !': event not found

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ python -c 'import adam\_atan2; print("Import erfolgreich!")'

Import erfolgreich!

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ python - <<'PY'

import torch

from adam\_atan2 import AdamATan2



print("GPU:", torch.cuda.get\_device\_name(0))



\# Testparameter auf GPU

w = torch.nn.Parameter(torch.randn(1024, device="cuda"))

optimizer = AdamATan2(\[w], lr=0.001)



\# Einen Optimierungsschritt durchführen

before = w.detach().clone()

loss = (w \*\* 2).mean()

loss.backward()

optimizer.step()

torch.cuda.synchronize()



print("Gewichte verändert:", not torch.equal(before, w))

print("AdamATan2 CUDA-Test erfolgreich!")

PY

GPU: NVIDIA GeForce GTX 1650 Ti

Gewichte verändert: True

AdamATan2 CUDA-Test erfolgreich!

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ python - <<'PY'

import torch

import triton



print("PyTorch:", torch.\_\_version\_\_)

print("Triton:", triton.\_\_version\_\_)

print("GPU:", torch.cuda.get\_device\_name(0))

print("Compute Capability:", torch.cuda.get\_device\_capability(0))



\# Einfache Funktion zum Kompilieren

def model(x):

&#x20;   return (torch.relu(x \* 1.5 + 0.2) \*\* 2).mean()



compiled\_model = torch.compile(model, backend="inductor")



\# Test auf der GPU

x = torch.randn(1024, 1024, device="cuda",

&#x20;               dtype=torch.float32, requires\_grad=True)



loss = compiled\_model(x)

loss.backward()

torch.cuda.synchronize()



print("Loss:", loss.item())

print("Gradienten berechnet:", x.grad is not None)

print("torch.compile erfolgreich!")

PY

PyTorch: 2.6.0+cu126

Triton: 3.2.0

GPU: NVIDIA GeForce GTX 1650 Ti

Compute Capability: (7, 5)

Loss: 1.3846678733825684

Gradienten berechnet: True

torch.compile erfolgreich!

(TRM) mathi@Schneller-Hobel:/tmp/adam-atan2$ cd ..

(TRM) mathi@Schneller-Hobel:/tmp$ cd ..

(TRM) mathi@Schneller-Hobel:/$ cd home

(TRM) mathi@Schneller-Hobel:/home$ cd mathi

(TRM) mathi@Schneller-Hobel:\~$ cd Thesis/

(TRM) mathi@Schneller-Hobel:\~/Thesis$ ls

hidden-spaces  wandb

(TRM) mathi@Schneller-Hobel:\~/Thesis$ cd hidden-spaces/

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ ls

README.md  code

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ wandb login wandb\_v1\_5cJQ9zstRTfIZ4XA0sEJDVn2J8W\_bdbxygnyMWIFKzRcj3u6iQSGBYEt40d1e9ws4BITu7V1jzhP6

Traceback (most recent call last):

&#x20; File "/home/mathi/miniconda3/envs/TRM/bin/wandb", line 6, in <module>

&#x20;   sys.exit(cli())

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1653, in \_\_call\_\_

&#x20;   return self.main(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1560, in main

&#x20;   rv = self.invoke(ctx)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 2054, in invoke

&#x20;   return \_process\_result(sub\_ctx.command.invoke(sub\_ctx))

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1414, in invoke

&#x20;   return ctx.invoke(self.callback, \*\*ctx.params)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 911, in invoke

&#x20;   return callback(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/cli/cli.py", line 137, in wrapper

&#x20;   return func(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/cli/cli.py", line 277, in login

&#x20;   wandb.login(

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 80, in login

&#x20;   return \_login(

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 325, in \_login

&#x20;   wlogin.try\_save\_api\_key(key)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 181, in try\_save\_api\_key

&#x20;   apikey.write\_key(self.\_settings, key)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/lib/apikey.py", line 313, in write\_key

&#x20;   raise ValueError(f"API key must be 40 characters long, yours was {len(key)}")

ValueError: API key must be 40 characters long, yours was 86

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ python -c "import torch; print(torch.cuda.is\_available())"

True

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ python -m pip install wandb==0.22.3

Collecting wandb==0.22.3

&#x20; Downloading wandb-0.22.3-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl.metadata (10 kB)

Requirement already satisfied: click>=8.0.1 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (8.5.1)

Requirement already satisfied: gitpython!=3.1.29,>=1.0.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (3.2.1)

Requirement already satisfied: packaging in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (24.1)

Requirement already satisfied: platformdirs in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (4.12.4)

Requirement already satisfied: protobuf!=4.21.0,!=5.28.0,<7,>=3.19.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (6.33.6)

Requirement already satisfied: pydantic<3 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (2.11.7)

Requirement already satisfied: pyyaml in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (6.0.3)

Requirement already satisfied: requests<3,>=2.0.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (2.34.2)

Requirement already satisfied: sentry-sdk>=2.0.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (2.74.0)

Requirement already satisfied: typing-extensions<5,>=4.8 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from wandb==0.22.3) (4.16.0)

Requirement already satisfied: annotated-types>=0.6.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from pydantic<3->wandb==0.22.3) (0.8.0)

Requirement already satisfied: pydantic-core==2.33.2 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from pydantic<3->wandb==0.22.3) (2.33.2)

Requirement already satisfied: typing-inspection>=0.4.0 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from pydantic<3->wandb==0.22.3) (0.4.5)

Requirement already satisfied: charset\_normalizer<4,>=2 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from requests<3,>=2.0.0->wandb==0.22.3) (3.5.2)

Requirement already satisfied: idna<4,>=2.5 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from requests<3,>=2.0.0->wandb==0.22.3) (3.20)

Requirement already satisfied: urllib3<3,>=1.26 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from requests<3,>=2.0.0->wandb==0.22.3) (2.8.0)

Requirement already satisfied: certifi>=2023.5.7 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from requests<3,>=2.0.0->wandb==0.22.3) (2026.10.23)

Requirement already satisfied: gitdb<5,>=4.0.1 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from gitpython!=3.1.29,>=1.0.0->wandb==0.22.3) (4.0.12)

Requirement already satisfied: smmap<6,>=3.0.1 in /home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.29,>=1.0.0->wandb==0.22.3) (5.0.3)

Downloading wandb-0.22.3-py3-none-manylinux\_2\_17\_x86\_64.manylinux2014\_x86\_64.whl (20.0 MB)

&#x20;  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.0/20.0 MB 9.7 MB/s  0:00:02

Installing collected packages: wandb

&#x20; Attempting uninstall: wandb

&#x20;   Found existing installation: wandb 0.21.3

&#x20;   Uninstalling wandb-0.21.3:

&#x20;     Successfully uninstalled wandb-0.21.3

Successfully installed wandb-0.22.3

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ wandb login

wandb: Logging into wandb.ai. (Learn how to deploy a W\&B server locally: https://wandb.me/wandb-server)

wandb: You can find your API key in your browser here: https://wandb.ai/authorize?ref=models

wandb: Paste an API key from your profile and hit enter, or press ctrl+c to quit:

Traceback (most recent call last):

&#x20; File "/home/mathi/miniconda3/envs/TRM/bin/wandb", line 6, in <module>

&#x20;   sys.exit(cli())

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1653, in \_\_call\_\_

&#x20;   return self.main(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1560, in main

&#x20;   rv = self.invoke(ctx)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 2054, in invoke

&#x20;   return \_process\_result(sub\_ctx.command.invoke(sub\_ctx))

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 1414, in invoke

&#x20;   return ctx.invoke(self.callback, \*\*ctx.params)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/click/core.py", line 911, in invoke

&#x20;   return callback(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/cli/cli.py", line 137, in wrapper

&#x20;   return func(\*args, \*\*kwargs)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/cli/cli.py", line 287, in login

&#x20;   wandb.login(

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 80, in login

&#x20;   logged\_in, \_ = \_login(

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 327, in \_login

&#x20;   wlogin.try\_save\_api\_key(key)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/wandb\_login.py", line 182, in try\_save\_api\_key

&#x20;   apikey.write\_key(self.\_settings, key)

&#x20; File "/home/mathi/miniconda3/envs/TRM/lib/python3.10/site-packages/wandb/sdk/lib/apikey.py", line 307, in write\_key

&#x20;   raise ValueError(

ValueError: API key must be at least 40 characters long, yours was 11

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ wandb login

wandb: Logging into wandb.ai. (Learn how to deploy a W\&B server locally: https://wandb.me/wandb-server)

wandb: You can find your API key in your browser here: https://wandb.ai/authorize?ref=models

wandb: Paste an API key from your profile and hit enter, or press ctrl+c to quit:

wandb: No netrc file found, creating one.

wandb: Appending key for api.wandb.ai to your netrc file: /home/mathi/.netrc

wandb: Currently logged in as: poematic (poematic-johannes-kepler-universitaet-linz) to https://api.wandb.ai. Use `wandb login --relogin` to force relogin

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ ls

README.md  code

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces$ cd code

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code$ ls

TRM  TinyRecursiveModels

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code$ git mv ./TinyRecursiveModels ./TRM/TinyRecursiveModels

(TRM) mathi@Schneller-Hobel:\~/Thesis/hidden-spaces/code$

