// show link to the latest clever firmware
gitbook.events.bind('page.change', function() {
	if (!document.querySelector('a.latest-firmware')) return;

	fetch('https://api.github.com/repos/CopterExpress/Firmware/releases').then(function (res) {
		return res.json();
	}).then(function (data) {
		// look for stable release
		let stable;
		for (let release of data) {
			let clever = (release.name.indexOf('clover') != -1) || (release.name.indexOf('clever') != -1);
			if (clever && !release.prerelease && !release.draft) {
				stable = release;
				break;
			}
		}

		// let el = document.querySelector('#download-latest-release');
		// el.innerHTML = stable.name;
		// el.href = stable.html_url;
		// document.querySelector('#release').style.display = 'block';
		for (let asset of stable.assets) {
			let el;
			if (asset.name == 'px4fmu-v4_default.px4') {
				el = document.querySelector('a.latest-firmware.v4');
			} else if (asset.name == 'px4fmu-v2_lpe.px4') {
				el = document.querySelector('a.latest-firmware.v2');
			}
			if (el) {
				el.href = asset.browser_download_url;
				el.innerHTML = stable.name;
			}
		}
	});
});

// show link to latest raspberry image
gitbook.events.bind('page.change', function() {
	var el = document.querySelector('a.latest-image');
	if (!el) return;

	// get latest release from GitHub
	fetch('https://api.github.com/repos/CopterExpress/clever/releases').then(function(res) {
		return res.json();
	}).then(function(data) {
		// look for stable release
		let stable;
		for (let release of data) {
			if (!release.prerelease && !release.draft) {
				stable = release;
				break;
			}
		}
		el.innerHTML = stable.name;
		el.href = stable.assets[0].browser_download_url;
	});
});
