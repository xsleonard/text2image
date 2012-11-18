#!/usr/bin/env python

import Image, ImageDraw, ImageFont

def get_args():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('outfile', help='File to save to')
    parser.add_argument('text', help='Text to render')
    parser.add_argument('font', help='Font file to use')
    parser.add_argument('fontsize', type=int, help='fontsize to use')
    parser.add_argument('--padding', metavar='N', type=int, nargs=2, help='x,y padding')
    
    return parser.parse_args()
    
def render(outfile, text, font, fontsize, padding=None):
    if padding is None:
        padding = (0,0)
        
    font = ImageFont.truetype(font, fontsize)
    size = font.getsize(text)
    size = tuple(map(lambda a: a[0] + 2*a[1], zip(size, padding)))
    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    draw.text(padding, text, font=font)
    image.save(outfile)

if __name__ == '__main__':
    args = get_args()
    render(args.outfile, args.text, args.font, args.fontsize, args.padding)
