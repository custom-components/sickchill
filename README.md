# Sickchill
  
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2019.svg?style=for-the-badge)](#) [![maintainer](https://img.shields.io/badge/maintainer-swetoast-blue.svg?style=for-the-badge)](#)  

Taps into the [Sickchill](https://sickchill.github.io/) API and lets you perform basic commands, like restart, daily searches, postprocess, etc.

To get started put the follwing files
```
/custom_components/sickchill/__init__.py
/custom_components/sickchill/services.yaml
```
into
```
<config directory>/custom_components/sickchill/__init__.py
<config directory>/custom_components/sickchill/services.yaml
```

**Example configuration.yaml:**

```yaml
sickchill:
  host: 'http://example.com:8081/api'
  api_key: 'your_api_key'
```
 
[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)  
***
Due to how `custom_components` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

~~Very early alpha run at own risk :) ~~ _Should work now :)_
