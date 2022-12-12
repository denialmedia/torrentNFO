![Alt text](/screenshots/2022-12-11_23-28.png?raw=true "Polybar Screenshot")
# torrentNFO

A Simple python script and module for polybar. 

## Description

I wanted an easy way to know when torrents where down downloading from my hosted qbBittorrent server. So I made a little script that lets you know what your downloads and uploads are. When clicked it should send a notification of what the last torrent added was. 

## Getting Started

### Dependencies

* You will need to install python-qbittorrent:
```
pip install python-qbittorrent
```
* qBittorent webUI must be enabled before using this API client. 

### Installing

You will want to add the grabNFO.py to wherever you keep your scripts for polybar. You will also need to make it executable.

```
chmod +x grabNFO.py
```

A simple Polybar module:
```
    [module/torrent]
    type = custom/script
    exec = grabNFO
    interval = .1
    format-prefix-font = 4
    format-prefix = "ó°šŒ "
    format-prefix-foreground = ${color.orange}
    format = <label>
    label-background= ${color.background}
    label-foreground = ${color.foreground}
    click-left = ~/.config/bspwm/scripts/grabNFO -o pop
```




## Help



## Authors


## Version History


* 0.1
    * Initial Release

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details

## Acknowledgments
