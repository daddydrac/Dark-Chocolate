import os, json
import pydash as _
import argparse as args


def coco_mixer(acc, curr):
      return _.flat_map(acc, lambda xo: {
        "id": curr['id'],
        "image_id": xo['image_id'],
        "coco_class": xo['category_id'],
        "x": xo['bbox'][0],
        "y": xo['bbox'][1],
        "bbox_width": xo['bbox'][2],
        "bbox_height": xo['bbox'][3],
        "img_width": curr['width'],
        "img_height": curr['height'],
        "output": curr['file_name']+".txt",
        "darkchocolate": [int(xo['category_id']) - 1, (xo['bbox'][0] + xo['bbox'][2] / 2) / curr['width'], (xo['bbox'][1] + xo['bbox'][3] / 2) / curr['height'], xo['bbox'][2] / curr['width'], xo['bbox'][3] / curr['height']
        ]
      }
   )


def dark_chocolate(_path):
    def ingredients(x, _path):
        with open(_path+'/' + x, 'r') as f:

            xoxo = _.reduce_right(json.load(f), coco_mixer)
            print(xoxo)

            if len(xoxo) > 0 and xoxo[0] != None:
                with open(str(xoxo[0]['output']), 'w') as makefile:
                    for item in xoxo:
                        object_id = str(item['darkchocolate'][0])
                        center_x = str(item['darkchocolate'][1])
                        center_y = str(item['darkchocolate'][2])
                        width = str(item['darkchocolate'][3])
                        height = str(item['darkchocolate'][4])

                        spaces = object_id + " " + center_x + " " + center_y + " " + width + " " + height

                        makefile.write('%s\n' % spaces)


    return _.map_([pos_json for pos_json in os.listdir(_path)
        if pos_json.endswith('.json')],
            lambda x: ingredients(x, _path))


if __name__ == '__main__':
    parser = args.ArgumentParser()
    parser.add_argument('--input-path', type=str, help='File path to COCO or custom COCO formatted annotations')
    opt = parser.parse_args()

    dark_chocolate(opt.input_path)

