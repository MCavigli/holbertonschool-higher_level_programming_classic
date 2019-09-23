#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.width += this.height;
    this.height = this.width - this.height;
    this.width -= this.height;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super();
    this.width = size;
    this.height = size;
  }
}
module.exports = Rectangle;
module.exports = Square;
