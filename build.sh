cmake -DCOMPUTE_BACKEND=cuda -DCMAKE_CUDA_COMPILER=/usr/local/cuda-12.8/bin/nvcc -S .
CUDA_VERSION=128 make  
pip install -e . 
