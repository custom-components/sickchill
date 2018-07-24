# Sickrage
  
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg?style=for-the-badge)](#) [![mantained](https://img.shields.io/maintenance/yes/2018.svg?style=for-the-badge)](#) [![maintainer](https://img.shields.io/badge/maintainer-swetoast-blue.svg?style=for-the-badge)](#)  

Taps into the [Sickrage](https://sickrage.github.io/) API and lets you perform basic commands, like restart, daily searches, postprocess, etc.

To get started put the follwing files
```
/custom_components/sickrage/__init__.py
/custom_components/sickrage/services.yaml
```
into
```
<config directory>/custom_components/sickrage/__init__.py
<config directory>/custom_components/sickrage/services.yaml
```

**Example configuration.yaml:**

```yaml
sickrage:
  host: 'http://example.com:8081/api'
  api_key: 'your_api_key'
```
 
[Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/)  
***
Due to how `custom_componentes` are loaded, it is normal to see a `ModuleNotFoundError` error on first boot after adding this, to resolve it, restart Home-Assistant.

~~Very early alpha run at own risk :) ~~ _Should work now :)_
