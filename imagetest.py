import lvgl as lv

from imagetools import get_png_info, open_png

from lv_colors import lv_colors

lv.init()
import SDL
SDL.init()
disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(480*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.buffer = disp_buf1
disp_drv.flush_cb = SDL.monitor_flush
disp_drv.hor_res = 480
disp_drv.ver_res = 320
disp_drv.register()

# Regsiter SDL mouse driver

indev_drv = lv.indev_drv_t()
indev_drv.init() 
indev_drv.type = lv.INDEV_TYPE.POINTER;
indev_drv.read_cb =SDL.mouse_read;
indev_drv.register();
#****************************************************************
from imagetools import get_png_info, open_png

# Register PNG image decoder
decoder = lv.img.decoder_create()
decoder.info_cb = get_png_info
decoder.open_cb = open_png

with open('param1.png','rb') as f:
  png_data = f.read()

png_img_dsc = lv.img_dsc_t({
    'data_size': len(png_data),
    'data': png_data 
})

# Create an image using the decoder

img1 = lv.img(lv.scr_act(),None)
lv.img.cache_set_size(2)
img1.align(lv.scr_act(), lv.ALIGN.CENTER, 0, -50)
img1.set_src(png_img_dsc)

img2 = lv.img(lv.scr_act(), None)
img2.set_src(lv.SYMBOL.OK+"Accept")
img2.align(img1, lv.ALIGN.OUT_BOTTOM_MID, 0, 20)
