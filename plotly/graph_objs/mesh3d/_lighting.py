from plotly.basedatatypes import BaseTraceHierarchyType


class Lighting(BaseTraceHierarchyType):

    # ambient
    # -------
    @property
    def ambient(self):
        """
        Ambient light increases overall color visibility but can wash
        out the image.
    
        The 'ambient' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['ambient']

    @ambient.setter
    def ambient(self, val):
        self['ambient'] = val

    # diffuse
    # -------
    @property
    def diffuse(self):
        """
        Represents the extent that incident rays are reflected in a
        range of angles.
    
        The 'diffuse' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['diffuse']

    @diffuse.setter
    def diffuse(self, val):
        self['diffuse'] = val

    # facenormalsepsilon
    # ------------------
    @property
    def facenormalsepsilon(self):
        """
        Epsilon for face normals calculation avoids math issues arising
        from degenerate geometry.
    
        The 'facenormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['facenormalsepsilon']

    @facenormalsepsilon.setter
    def facenormalsepsilon(self, val):
        self['facenormalsepsilon'] = val

    # fresnel
    # -------
    @property
    def fresnel(self):
        """
        Represents the reflectance as a dependency of the viewing
        angle; e.g. paper is reflective when viewing it from the edge
        of the paper (almost 90 degrees), causing shine.
    
        The 'fresnel' property is a number and may be specified as:
          - An int or float in the interval [0, 5]

        Returns
        -------
        int|float
        """
        return self['fresnel']

    @fresnel.setter
    def fresnel(self, val):
        self['fresnel'] = val

    # roughness
    # ---------
    @property
    def roughness(self):
        """
        Alters specular reflection; the rougher the surface, the wider
        and less contrasty the shine.
    
        The 'roughness' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['roughness']

    @roughness.setter
    def roughness(self, val):
        self['roughness'] = val

    # specular
    # --------
    @property
    def specular(self):
        """
        Represents the level that incident rays are reflected in a
        single direction, causing shine.
    
        The 'specular' property is a number and may be specified as:
          - An int or float in the interval [0, 2]

        Returns
        -------
        int|float
        """
        return self['specular']

    @specular.setter
    def specular(self, val):
        self['specular'] = val

    # vertexnormalsepsilon
    # --------------------
    @property
    def vertexnormalsepsilon(self):
        """
        Epsilon for vertex normals calculation avoids math issues
        arising from degenerate geometry.
    
        The 'vertexnormalsepsilon' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        return self['vertexnormalsepsilon']

    @vertexnormalsepsilon.setter
    def vertexnormalsepsilon(self, val):
        self['vertexnormalsepsilon'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'mesh3d'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
        facenormalsepsilon
            Epsilon for face normals calculation avoids math issues
            arising from degenerate geometry.
        fresnel
            Represents the reflectance as a dependency of the
            viewing angle; e.g. paper is reflective when viewing it
            from the edge of the paper (almost 90 degrees), causing
            shine.
        roughness
            Alters specular reflection; the rougher the surface,
            the wider and less contrasty the shine.
        specular
            Represents the level that incident rays are reflected
            in a single direction, causing shine.
        vertexnormalsepsilon
            Epsilon for vertex normals calculation avoids math
            issues arising from degenerate geometry.
        """

    def __init__(
        self,
        ambient=None,
        diffuse=None,
        facenormalsepsilon=None,
        fresnel=None,
        roughness=None,
        specular=None,
        vertexnormalsepsilon=None,
        **kwargs
    ):
        """
        Construct a new Lighting object
        
        Parameters
        ----------
        ambient
            Ambient light increases overall color visibility but
            can wash out the image.
        diffuse
            Represents the extent that incident rays are reflected
            in a range of angles.
        facenormalsepsilon
            Epsilon for face normals calculation avoids math issues
            arising from degenerate geometry.
        fresnel
            Represents the reflectance as a dependency of the
            viewing angle; e.g. paper is reflective when viewing it
            from the edge of the paper (almost 90 degrees), causing
            shine.
        roughness
            Alters specular reflection; the rougher the surface,
            the wider and less contrasty the shine.
        specular
            Represents the level that incident rays are reflected
            in a single direction, causing shine.
        vertexnormalsepsilon
            Epsilon for vertex normals calculation avoids math
            issues arising from degenerate geometry.

        Returns
        -------
        Lighting
        """
        super(Lighting, self).__init__('lighting')

        # Import validators
        # -----------------
        from plotly.validators.mesh3d import (lighting as v_lighting)

        # Initialize validators
        # ---------------------
        self._validators['ambient'] = v_lighting.AmbientValidator()
        self._validators['diffuse'] = v_lighting.DiffuseValidator()
        self._validators['facenormalsepsilon'
                        ] = v_lighting.FacenormalsepsilonValidator()
        self._validators['fresnel'] = v_lighting.FresnelValidator()
        self._validators['roughness'] = v_lighting.RoughnessValidator()
        self._validators['specular'] = v_lighting.SpecularValidator()
        self._validators['vertexnormalsepsilon'
                        ] = v_lighting.VertexnormalsepsilonValidator()

        # Populate data dict with properties
        # ----------------------------------
        self.ambient = ambient
        self.diffuse = diffuse
        self.facenormalsepsilon = facenormalsepsilon
        self.fresnel = fresnel
        self.roughness = roughness
        self.specular = specular
        self.vertexnormalsepsilon = vertexnormalsepsilon

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**kwargs)