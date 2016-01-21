

import React, { Component } from 'react';
import L from 'leaflet';
import { findDOMNode } from 'react-dom';

import 'leaflet.Zoomify';


const size = 35000;


export default class extends Component {


  /**
   * Spin up the leaflet instance.
   */
  componentDidMount() {

    let el = findDOMNode(this.refs.image);

    this.map = L.map(el, {
      crs: L.CRS.Simple,
      zoomControl: false,
    });

    let zoomControl = L.control.zoom({
      position: 'topright',
    });

    this.map.addControl(zoomControl);

    let layer = L.tileLayer.zoomify('/static/tiles/', {
      width: size,
      hwight: size,
    });

    this.map.addLayer(layer);
    console.log(this.map);

  }


  /**
   * Render the image container.
   */
  render() {
    return <div id="image" ref="image"></div>;
  }


}
