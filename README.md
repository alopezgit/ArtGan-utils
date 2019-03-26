# ArtGan-utils

First we need to install torch.

Follow http://torch.ch/docs/getting-started.html

You may need to install cmake and set path via

```
export PATH=CMAKE_PATH/bin:$PATH
```

Things done to install Torch:

Solve incompatibility CUDA9.0 and Torch (reason half-precision operators) 

```
export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"
```

And maybe also use gcc6

```
sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-6 10
```

```
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 10
```

generate_cnn_features.py: generate the image features from a pretrained net.
data_format_embeddings.py: here I am trying to set up the files in the same format as in the CVPR16 code.
tensors_to_t7.lua: Transforms the numpy image features to t7, which is the format needed by torch.

To do: I think I need to encode the text in a t7 to make it work. So map text (string format) to vector and then save to t7. 

