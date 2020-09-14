from fastai.vision.all import *

def run():
    torch.multiprocessing.freeze_support()
    path = Path("E:/GateCrash/")
    fnames = get_image_files(path)
    print(f"Total Images:{len(fnames)}")


    def label_func(x): return x.parent.name

    dls = ImageDataLoaders.from_path_func(path, fnames, label_func, num_workers=0)


    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    path = Path("C:/Users/programmer/Desktop/FallGuys")
    learn_inf = learn.load("C:/Users/programmer/Desktop/FallGuys/agent.save")
    learn_inf.predict('g1-j5.png')
    learn.export()

if __name__ == '__main__':
    run()
