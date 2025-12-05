from concurrent.futures import ProcessPoolExecutor
from functools import partial
from multiprocessing import Pool

from knotprot_download import *

def run_download_seq(my_dir):
    proteins = get_proteins()
    i = 0
    for p in proteins:
        download_link(my_dir, p)
        i += 1
    print(f'Downloaded: {i} images')


def run_download_parall(my_dir):
    proteins = get_proteins()
    download_func = partial(download_link, my_dir)
    with Pool(processes=8) as pool:
        pool.map(download_func, proteins)


def run_thumbnails_seq(my_dir):
    image_files = Path(my_dir).iterdir()
    for f in image_files:
        create_thumbnail((324, 324), f)


def run_thumbnails_parall(my_dir):
    image_files = Path(my_dir).iterdir()
    create_thumbnail_func = partial(create_thumbnail, (324, 324))
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(create_thumbnail_func, image_files)


if __name__ == '__main__':
    my_dir = 'images'
    #setup_download_dir(my_dir)
    #run_download_seq(my_dir)
    #time_it(run_download_seq, my_dir)
    #time_it(run_download_parall, my_dir)
    #time_it(run_thumbnails_seq, my_dir)
    time_it(run_thumbnails_parall, my_dir)