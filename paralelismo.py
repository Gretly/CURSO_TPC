import os
import time
import logging
import multiprocessing

logging.basicConfig(level=logging.DEBUG, format='%(message)s')

def new_process(time_to_sleep=0):
    logging.info('PROCESO: EDITAMOS UN VIDEO')

    time.sleep(time_to_sleep)

    logging.info('PROCESO: CREDITOS DEL VIDEO')

def main():
    process = multiprocessing.Process(target=new_process,
                                        name='PRODESO_EDICION',
                                        args=(1,),
                                        daemon=False)
    process.start()
    process.join()

    logging.info(f'ENTREGAMOS EL PRODUCTO')

if __name__ == '__main__':
    main()