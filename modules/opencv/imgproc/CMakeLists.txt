ectomodule(imgproc
    module.cpp
    Adder.cpp
    BilateralFilter.cpp
    BitWiseAnd.cpp
    BitWiseNot.cpp
    CartToPolar.cpp
    cvtColor.cpp
    GaussianBlur.cpp
    NanRemove.cpp
    Scale.cpp
    Scharr.cpp
    Sobel.cpp
    Translate.cpp
    )

link_ecto(imgproc ${OpenCV_LIBS})
install_ecto_module(imgproc)