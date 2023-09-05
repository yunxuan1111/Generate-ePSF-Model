def build_epsf(self, stars, *, init_epsf=None):
        """
        Build iteratively an ePSF from star cutouts.

        Parameters
        ----------
        stars : `EPSFStars` object
            The stars used to build the ePSF.

        init_epsf : `EPSFModel` object, optional
            The initial ePSF model.  If not input, then the ePSF will be
            built from scratch.

        Returns
        -------
        epsf : `EPSFModel` object
            The constructed ePSF.

        fitted_stars : `EPSFStars` object
            The input stars with updated centers and fluxes derived
            from fitting the output ``epsf``.
        """
        
        """
        iter_num = 0
        n_stars = stars.n_stars
        fit_failed = np.zeros(n_stars, dtype=bool)
        epsf = init_epsf
        center_dist_sq = self.center_accuracy_sq + 1.0
        centers = stars.cutout_center_flat


        if self.progress_bar and HAS_TQDM:
            from tqdm.auto import tqdm
            pbar_desc = f'EPSFBuilder ({self.maxiters} maxiters)'
            pbar = tqdm(total=self.maxiters, desc=pbar_desc)
        else:
            pbar = None
        """

        
        # build the ePSF
        epsf = init_epsf
        epsf = self._build_epsf_step(stars, epsf=epsf)
        return epsf, stars
        


        # Since maxiters = 1, we don't need this part
        """
        while (iter_num < self.maxiters and not np.all(fit_failed)
               and np.max(center_dist_sq) >= self.center_accuracy_sq):

            iter_num += 1

            # build/improve the ePSF
            epsf = self._build_epsf_step(stars, epsf=epsf)

            # fit the new ePSF to the stars to find improved centers
            # we catch fit warnings here -- stars with unsuccessful fits
            # are excluded from the ePSF build process
            with warnings.catch_warnings():
                message = '.*The fit may be unsuccessful;.*'
                warnings.filterwarnings('ignore', message=message,
                                        category=AstropyUserWarning)
                stars = self.fitter(epsf, stars)

            # find all stars where the fit failed
            fit_failed = np.array([star._fit_error_status > 0
                                   for star in stars.all_stars])
            if np.all(fit_failed):
                raise ValueError('The ePSF fitting failed for all stars.')

            # permanently exclude fitting any star where the fit fails
            # after 3 iterations
            
            
            if iter_num > 3 and np.any(fit_failed):
                idx = fit_failed.nonzero()[0]
                for i in idx:  # pylint: disable=not-an-iterable
                    stars.all_stars[i]._excluded_from_fit = True
            

            # if no star centers have moved by more than pixel accuracy,
            # stop the iteration loop early
            dx_dy = stars.cutout_center_flat - centers
            dx_dy = dx_dy[np.logical_not(fit_failed)]
            center_dist_sq = np.sum(dx_dy * dx_dy, axis=1, dtype=np.float64)
            centers = stars.cutout_center_flat

            self._epsf.append(epsf)

            if pbar is not None:
                pbar.update()
        
            
        if pbar is not None:
            if iter_num < self.maxiters:
                pbar.write(f'EPSFBuilder converged after {iter_num} '
                           f'iterations (of {self.maxiters} maximum '
                           'iterations)')
            pbar.close()

        return epsf, stars
        """