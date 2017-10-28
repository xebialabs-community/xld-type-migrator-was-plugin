# XL Deploy Type Migrator WAS plugin v1.0.0

[![Build Status][xld-type-migrator-was-plugin-travis-image]][xld-type-migrator-was-plugin-travis-url]
[![License: MIT][xld-type-migrator-was-plugin-license-image]][xld-type-migrator-was-plugin-license-url]
![Github All Releases][xld-type-migrator-was-plugin-downloads-image]

[xld-type-migrator-was-plugin-travis-image]: https://travis-ci.org/xebialabs-community/xld-type-migrator-was-plugin.svg?branch=master
[xld-type-migrator-was-plugin-travis-url]: https://travis-ci.org/xebialabs-community/xld-type-migrator-was-plugin
[xld-type-migrator-was-plugin-license-image]: https://img.shields.io/badge/License-MIT-yellow.svg
[xld-type-migrator-was-plugin-license-url]: https://opensource.org/licenses/MIT
[xld-type-migrator-was-plugin-downloads-image]: https://img.shields.io/github/downloads/xebialabs-community/xld-type-migrator-was-plugin/total.svg

## Preface

This document describes the functionality provided by the XL [Deploy|Release] [Description|Interface] plugin.

See the [XL Deploy reference manual](https://docs.xebialabs.com/xl-deploy) for background information on XL Deploy and deployment automation concepts.  

## Overview

This plugin maps the properties of the was.ServerConfigurationSpec to the was.JavaProcessDefinitionSpec for migration.

## Requirements

* XL Deploy 5.5

## Installation

* Copy the latest JAR file from the [releases page](https://github.com/xebialabs-community/xld-type-migrator-was-plugin/releases) into the `XL_DEPLOY_SERVER/plugins` directory.
* Restart the XL Deploy server.

## Usage

Use this plugin in combination with the [XL Deploy Type Migrator plugin](https://github.com/xebialabs-community/xld-type-migrator-plugin).

## References

[XL Deploy WAS plugin](https://docs.xebialabs.com/xl-deploy-was-plugin/7.0.x/wasPluginManual.html)



