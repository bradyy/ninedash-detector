YOLOv5(m) okayish-trained ninedash detector

Code contains webapp + RESTful API, you probably need to edit it to fit your usage.

Zalo AI competitor, not really, but free.

web demo: https://api.lets-rp.com/ninedash/
api: https://api.lets-rp.com/v1/ninedash/detect

example json return data:
```{
    "have_ninedash": 1,
    "locations": [
        {
            "bbox": {
                "x_center": 343.1834716796875,
                "y_center": 271.02252197265625,
                "width": 243.12103271484375,
                "height": 335.51605224609375
            },
            "score": 0.943516194820404
        },
        {
            "bbox": {
                "x_center": 850.6929931640625,
                "y_center": 248.51612854003906,
                "width": 242.1363525390625,
                "height": 340.3798522949219
            },
            "score": 0.9317539930343628
        }
    ]
}
```

if have_ninedash is 0, locations is undefined.

