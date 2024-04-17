*IMPORTANT: install torch BEFORE install mmcv-full
torch.version
'1.9.0+cu111'
mmcv.version
'2.0.0rc4'
mmdet.version
'3.0.0'

# install mmengine
git clone https://github.com/open-mmlab/mmengine.git
cd mmengine
pip install -e . -v

install torch https://pytorch.org/get-started/previous-versions/ 
check torch version
python -c 'import torch;print(torch.__version__);print(torch.version.cuda)'

install mmcv 
pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/{cu_version}/{torch_version}/index.html
pip install mmcv==2.0.0rc4 -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.9/index.html

install mmdet
git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .

download checkpoint 
check it works
 python3 demo/image_demo.py demo/demo.jpg configs/rtmdet/rtmdet_tiny_8xb32-300e_coco.py --weights rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth --device cpu --show
'''


'''
# Bug
**TYPE: ModuleNotFoundError: No module named 'mmcv._ext'
->  

    pip uninstall mmcv-full
    
    pip install mmcv
    
    re-run this program, make sure it raise ImportError: mmcv not found
    
    reinstall mmcv-full with pip install openmim; mim install mmcv-full, or other version based on your requirements.
    
-> downgrade: mmcv==0.6.2 and mmdet==2.3.0 .

-> pyinstaller --hidden-import=mmcv._ext --hidden-import torchvision --onefile our_python_file.py.

Explain:

  While running pyinstaller, add --hidden-import with the path to your mmcv.
  While installing PyTorch, i only want to use CPU version, so in homepage of PyTorch, i use pip-cpu-version install command.

->If you install it via pip install mmcv, the lite version is installed, which does not contain mmcv._ext.-> No module name: 'mmcv'.

-> pip install mmcv==2.0.1 -f https://download.openmmlab.com/mmcv/dist/cu117/torch2.0/index.html

->:first: 

    pip uninstall mmcv
:then: 

    pip install mmcv-full==latest+torch1.5.0+cu101 -f https://download.openmmlab.com/mmcv/dist/index.html
-> I TRIED UNINSTALL TORCH AND NVIDIA AND THEN I INSTALL IT AGAIN : "I deleted and reinstalled because I want Torch and CUDA to be integrated."->AssertionError: Torch not compiled with CUDA enabled.

-> 
     
    pip uninstall mmcv
    pip uninstall mmcv-full
    git clone https://github.com/open-mmlab/mmcv.git
    cd mmcv
    set MMCV_WITH_OPS=1
    pip install -e .


....

===> nothing changed


**RUN WITH .VENV ENVIRONMENT
*TYPE: ModuleNotFoundError: No module named 'mmcv._ext'
*Type: No CUDA runtime is found


