# Dark Chocolate #

Transfer COCO data set annotations to Darknet YOLO annotations format. Hence, Dark(net) Chocolate(COCO)!

### How to run the coco mixer
1. Open the command line
2. Type in:  ```python dark_chocolate.py --input-path ../my/file/path/here```

### Validation - Explain your AI from the pipeline forward
When you run the command line util, it will output the JSON for each so you can validate class IDs, as well the math for any changes/updates in Darknet or COCO, etc.

```
[  
   {  
      'id':260,
      'image_id':260,
      # make sure the two image IDs match
      
      'coco_class':'3',
      # make sure the class ID matches the index position in *.names file for COCO that Darknet looks at for obj detection
      
      'x':529,
      'y':218,
      # full width and height of the entire bounding box 
      
      'bbox_width':89,
      'bbox_height':77,
      # bounding box coords where, in this case, x is 89px from right and y is 77px down the image
      
      'img_width':640,
      'img_height':512,
      # the width and height of the entire image
      
      'output':'FLIR_00260.txt',
      # must match image name
      
      'darkchocolate':[  
         3,
         0.8265625,
         0.42578125,
         0.1390625,
         0.150390625
      ]
      # The 'darkchocolate' key contains the values that will be output in *.txt file in darknet format
   }
]
```

### The Math for Darknet Annotation Conversion
This represents the output, in the order that you will see in *.txt files from the JSON object generated above:
```
(class id) ((x + bbox_width / 2)  / img_width), ((y + bbox_height / 2) / img_height), (bbox_width / img_width), (bbox_height / img_height)
```

#### Support
Yolov3, Current version of COCO and Linux are only supported at this time


