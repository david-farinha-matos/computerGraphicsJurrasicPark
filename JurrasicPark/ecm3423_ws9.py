import pygame

# import the scene class
from cubeMap import FlattenCubeMap
from scene import Scene

from lightSource import LightSource

from blender import load_obj_file

from BaseModel import DrawModelFromMesh

from shaders import *

from ShadowMapping import *

from sphereModel import Sphere

from skyBox import *

from environmentMapping import *

from math import sin, cos, radians

class ExeterScene(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.light = LightSource(self, position=[3., 6, -7.])

        self.shaders='phong'

        # for shadow map rendering
        self.shadows = ShadowMap(light=self.light)
        self.show_shadow_map = ShowTexture(self, self.shadows)

        # Load the objects
        meshes = load_obj_file('models/LongRoad.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0,-3.6,0]),scaleMatrix([0.6,0.6,0.6])), mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='scene') for mesh in meshes]
        )
        meshes = load_obj_file('models/LongRoadPave.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0, -3.61, 2]), scaleMatrix([0.6, 0.6, 0.6])),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='scene') for mesh in
             meshes]
        )
        meshes = load_obj_file('models/LongRoadPave.obj')
        self.add_models_list(
            [DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0, -3.61, -2]), scaleMatrix([0.6, 0.6, 0.6])),
                               mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='scene') for mesh in
             meshes]
        )

        house3 = load_obj_file('models/House.obj')
        house4 = load_obj_file('models/House.obj')
        industrialBuilding2 = load_obj_file('models/industrial_biulding.obj')
        tank2 = load_obj_file('models/tank_trexhwm.obj')
        barrier2 = load_obj_file('models/Concrete_Barricade.obj')

        # Define the translation and scaling matrices for house 3
        translation_matrix_house3 = translationMatrix([2.5, -3.1, 5.5])
        scaling_matrix_house3 = scaleMatrix([0.4, 0.4, 0.4])

        # Define the translation and scaling matrices for house 4
        translation_matrix_house4 = translationMatrix([7.6, -3.1, 5.5])
        scaling_matrix_house4 = scaleMatrix([0.4, 0.4, 0.4])

        translation_matrix_industrial2 = translationMatrix([5.3,-2.6,-4.55])
        scaling_matrix_industrial2 = scaleMatrix([0.25, 0.25, 0.25])

        translation_matrix_tank2 = translationMatrix([-2, -3, -1])
        scaling_matrix_tank2 = scaleMatrix([0.2, 0.2, 0.2])

        translation_matrix_barrier2 = translationMatrix([4.8, -2.9, 0.3])
        scaling_matrix_barrier2 = scaleMatrix([0.7, 0.7, 0.7])

        # Define the rotation matrix for rotating around the Y-axis by 90 degrees
        rotation_angle_radians_house = radians(180)  # Convert degrees to radians
        rotation_angle_radians_tank2 = radians(340)  # Convert degrees to radians
        rotation_angle_radians_barrier2 = radians(340)  # Convert degrees to radians

        # Create the rotation matrix for Y-axis
        rotation_matrix_house = np.array([
            [cos(rotation_angle_radians_house), 0, sin(rotation_angle_radians_house), 0],
            [0, 1, 0, 0],
            [-sin(rotation_angle_radians_house), 0, cos(rotation_angle_radians_house), 0],
            [0, 0, 0, 1]
        ])
        rotation_matrix_tank2 = np.array([
            [cos(rotation_angle_radians_tank2), 0, sin(rotation_angle_radians_tank2), 0],
            [0, 1, 0, 0],
            [-sin(rotation_angle_radians_tank2), 0, cos(rotation_angle_radians_tank2), 0],
            [0, 0, 0, 1]
        ])
        rotation_matrix_barrier2 = np.array([
            [cos(rotation_angle_radians_barrier2), 0, sin(rotation_angle_radians_barrier2), 0],
            [0, 1, 0, 0],
            [-sin(rotation_angle_radians_barrier2), 0, cos(rotation_angle_radians_barrier2), 0],
            [0, 0, 0, 1]
        ])

        # Combine all transformation matrices house 3
        combined_matrix_house3 = np.matmul(translation_matrix_house3, scaling_matrix_house3)
        combined_matrix_house3 = np.matmul(combined_matrix_house3, rotation_matrix_house)

        # Combine all transformation matrices house 4
        combined_matrix_house4 = np.matmul(translation_matrix_house4, scaling_matrix_house4)
        combined_matrix_house4 = np.matmul(combined_matrix_house4, rotation_matrix_house)

        # Combine all transformation matrices industrial house 2
        combined_matrix_industrial2 = np.matmul(translation_matrix_industrial2, scaling_matrix_industrial2)
        combined_matrix_industrial2 = np.matmul(combined_matrix_industrial2, rotation_matrix_house)

        # Combine all transformation matrices industrial tank 2
        combined_matrix_tank2 = np.matmul(translation_matrix_tank2, scaling_matrix_tank2)
        combined_matrix_tank2 = np.matmul(combined_matrix_tank2, rotation_matrix_tank2)

        # Combine all transformation matrices industrial barrier 2
        combined_matrix_barrier2 = np.matmul(translation_matrix_barrier2, scaling_matrix_barrier2)
        combined_matrix_barrier2 = np.matmul(combined_matrix_barrier2, rotation_matrix_barrier2)

        house1 = load_obj_file('models/industrial_biulding.obj')
        self.house1 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([-4.2,-2.6,3.95]), scaleMatrix([0.25, 0.25, 0.25])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='house1') for mesh in
            house1]
        self.industrialBuilding2 = [
            DrawModelFromMesh(scene=self,
                              M=combined_matrix_industrial2,
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='industrialBuilding2') for mesh in
            industrialBuilding2]
        house2 = load_obj_file('models/House.obj')
        self.house2 = [
            DrawModelFromMesh(scene=self,
                              M=np.matmul(translationMatrix([-6.5, -3.1, -6.1]), scaleMatrix([0.4, 0.4, 0.4])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='house2') for mesh in
            house2]
        self.house3 = [
            DrawModelFromMesh(scene=self,
                              M=combined_matrix_house3,
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='house3') for mesh in
            house3]
        self.house4 = [
            DrawModelFromMesh(scene=self,
                              M=combined_matrix_house4,
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='house4') for mesh in
            house4]
        house5 = load_obj_file('models/House.obj')
        self.house5 = [
            DrawModelFromMesh(scene=self,
                              M=np.matmul(translationMatrix([-1.4, -3.1, -6.1]), scaleMatrix([0.4, 0.4, 0.4])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='house5') for mesh in
            house5]

        tank = load_obj_file('models/tank_trexhwm.obj')
        self.tank = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([-5, -3, 0]), scaleMatrix([0.2, 0.2, 0.2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='tank') for mesh in
            tank]
        self.tank2 = [
            DrawModelFromMesh(scene=self,
                              M=combined_matrix_tank2,
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='tank2') for mesh in
            tank2]
        lamppost1 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost1 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([-8, -2.9, 1.2]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost1') for mesh in
            lamppost1]
        lamppost2 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost2 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0, -2.9, 1.2]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost2') for mesh
            in
            lamppost2]
        lamppost3 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost3 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([8, -2.9, 1.2]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost3') for mesh
            in
            lamppost3]
        lamppost4 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost4 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([0, -2.9, -1.9]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost4') for mesh
            in
            lamppost4]
        lamppost5 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost5 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([-8, -2.9, -1.9]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost5') for mesh
            in
            lamppost5]
        lamppost6 = load_obj_file('models/Street_lamp_1.obj')
        self.lamppost6 = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([8, -2.9, -1.9]), scaleMatrix([2, 2, 2])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='lamppost6') for mesh
            in
            lamppost6]
        barrier = load_obj_file('models/Concrete_Barricade.obj')
        self.barrier = [
            DrawModelFromMesh(scene=self, M=np.matmul(translationMatrix([5, -2.9, -1]), scaleMatrix([0.7, 0.7, 0.7])),
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='barrier') for mesh
            in
            barrier]
        self.barrier2 = [
            DrawModelFromMesh(scene=self,
                              M=combined_matrix_barrier2,
                              mesh=mesh, shader=ShadowMappingShader(shadow_map=self.shadows), name='barrier2') for mesh in
            barrier2]

        # draw a skybox for the horizon
        self.skybox = SkyBox(scene=self)

        self.show_light = DrawModelFromMesh(scene=self, M=poseMatrix(position=self.light.position, scale=0.2), mesh=Sphere(material=Material(Ka=[10,10,10])), shader=FlatShader())

        self.environment = EnvironmentMappingTexture(width=400, height=400)

        bin1 = load_obj_file('models/Trashcan.obj')
        self.bin1 = DrawModelFromMesh(
            scene=self,
            M=np.matmul(translationMatrix([0, -2.9, 1.5]), scaleMatrix([0.2, 0.2, 0.2])),
            mesh=bin1[0],
            shader=EnvironmentShader(map=self.environment),
            name='bin1'
        )
        self.add_models_list([self.bin1])

        bin2 = load_obj_file('models/Trashcan.obj')
        self.bin2 = DrawModelFromMesh(
            scene=self,
            M=np.matmul(translationMatrix([5.5, -2.9, 2]), scaleMatrix([0.2, 0.2, 0.2])),
            mesh=bin2[0],
            shader=EnvironmentShader(map=self.environment),
            name='bin2'
        )
        self.add_models_list([self.bin2])

        dinosaur = load_obj_file('models/toy-dino.obj')
        self.dinosaur = DrawModelFromMesh(
            scene=self,
            M=np.matmul(translationMatrix([2, -2.9, 0.8]), scaleMatrix([0.4, 0.4, 0.4])),
            mesh=dinosaur[0],
            shader=ShadowMappingShader(shadow_map=self.shadows),
            name='dinosaur'
        )
        self.add_models_list([self.dinosaur])

        # Define the dinosaur's initial position
        self.dinosaur_position = np.array([0.0, 0.0, 0.0])
        self.dinosaur_speed = 0.5  # Adjust the speed of movement as needed
        self.dinosaur_rotation_angle = 10.0  # Adjust the rotation angle as needed

        # rotate on/off function
        self.rotateFlagger = False
        self.rotation_angle = 10  # Rotation angle increment

        self.moveForwardFlagger = False


        self.flattened_cube = FlattenCubeMap(scene=self, cube=self.environment)


        # rotate on/off function
        self.rotateFlagger = False

    def draw_shadow_map(self):
        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # also all models from the table
        for model in self.tank:
            model.draw()
        # and for the house1
        for model in self.house1:
            model.draw()
        for model in self.house2:
            model.draw()
        for model in self.house3:
            model.draw()
        for model in self.house4:
            model.draw()
        for model in self.house5:
            model.draw()
        for model in self.industrialBuilding2:
            model.draw()
        for model in self.lamppost1:
            model.draw()
        for model in self.lamppost2:
            model.draw()
        for model in self.lamppost3:
            model.draw()
        for model in self.lamppost4:
            model.draw()
        for model in self.lamppost5:
            model.draw()
        for model in self.lamppost6:
            model.draw()
        for model in self.tank2:
            model.draw()
        for model in self.barrier:
            model.draw()
        for model in self.barrier2:
            model.draw()

    def draw_reflections(self):
        self.skybox.draw()

        for model in self.models:
            model.draw()

        # # also all models from the tank
        for model in self.tank:
            model.draw()
        # and for the tank
        for model in self.house1:
            model.draw()
        for model in self.house2:
            model.draw()
        for model in self.house3:
            model.draw()
        for model in self.house4:
            model.draw()
        for model in self.house5:
            model.draw()
        for model in self.industrialBuilding2:
            model.draw()
        for model in self.lamppost1:
            model.draw()
        for model in self.lamppost2:
            model.draw()
        for model in self.lamppost3:
            model.draw()
        for model in self.lamppost4:
            model.draw()
        for model in self.lamppost5:
            model.draw()
        for model in self.lamppost6:
            model.draw()
        for model in self.tank2:
            model.draw()
        for model in self.barrier:
            model.draw()
        for model in self.barrier2:
            model.draw()



    def draw(self, framebuffer=False):
        '''
        Draw all models in the scene
        :return: None
        '''

        # first we need to clear the scene, we also clear the depth buffer to handle occlusions
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # when using a framebuffer, we do not update the camera to allow for arbitrary viewpoint.
        if not framebuffer:
            self.camera.update()

        if not framebuffer:
            self.rotate_dinosaur()
            self.move_dinosaur_forward()

        # first, we draw the skybox
        self.skybox.draw()

        # render the shadows
        self.shadows.render(self)

        # when rendering the framebuffer we ignore the reflective object
        if not framebuffer:

            self.environment.update(self)

            self.bin1.draw()
            self.bin2.draw()
            self.dinosaur.draw()

            # if enabled, show flattened cube
            self.flattened_cube.draw()


            self.show_shadow_map.draw()

        # then we loop over all models in the list and draw them
        for model in self.models:
            model.draw()

        # also all models from the tank
        for model in self.tank:
            model.draw()
        # and for the tank
        for model in self.house1:
            model.draw()
        for model in self.house2:
            model.draw()
        for model in self.house3:
            model.draw()
        for model in self.house4:
            model.draw()
        for model in self.house5:
            model.draw()
        for model in self.industrialBuilding2:
            model.draw()
        for model in self.lamppost1:
            model.draw()
        for model in self.lamppost2:
            model.draw()
        for model in self.lamppost3:
            model.draw()
        for model in self.lamppost4:
            model.draw()
        for model in self.lamppost5:
            model.draw()
        for model in self.lamppost6:
            model.draw()
        for model in self.tank2:
            model.draw()
        for model in self.barrier:
            model.draw()
        for model in self.barrier2:
            model.draw()

        self.show_light.draw()

        # once we are done drawing, we display the scene
        # Note that here we use double buffering to avoid artefacts:
        # we draw on a different buffer than the one we display,
        # and flip the two buffers once we are done drawing.
        if not framebuffer:
            pygame.display.flip()

    def keyboard(self, event):
        '''
        Process additional keyboard events for this demo.
        '''
        Scene.keyboard(self, event)

        if event.key == pygame.K_c:
            if self.flattened_cube.visible:
                self.flattened_cube.visible = False
            else:
                print('--> showing cube map')
                self.flattened_cube.visible = True

        if event.key == pygame.K_s:
            if self.show_shadow_map.visible:
                self.show_shadow_map.visible = False
            else:
                print('--> showing shadow map')
                self.show_shadow_map.visible = True

        if event.key == pygame.K_1:
            print('--> using Flat shading')
            self.bin1.use_textures = True
            self.bin1.bind_shader('flat')

        if event.key == pygame.K_2:
            print('--> using Phong shading')
            self.bin1.use_textures = True
            self.bin1.bind_shader('phong')

        elif event.key == pygame.K_4:
            print('--> using original texture')
            self.bin1.shader.mode = 1

        elif event.key == pygame.K_6:
            self.bin1.mesh.material.alpha += 0.1
            print('--> bin1 alpha={}'.format(self.bin1.mesh.material.alpha))
            if self.bin1.mesh.material.alpha > 1.0:
                self.bin1.mesh.material.alpha = 0.0

        elif event.key == pygame.K_7:
            print('--> no face culling')
            glDisable(GL_CULL_FACE)

        elif event.key == pygame.K_8:
            print('--> glCullFace(GL_FRONT)')
            glEnable(GL_CULL_FACE)
            glCullFace(GL_FRONT)

        elif event.key == pygame.K_9:
            print('--> glCullFace(GL_BACK)')
            glEnable(GL_CULL_FACE)
            glCullFace(GL_BACK)

        elif event.key == pygame.K_BACKQUOTE:
            if glIsEnabled(GL_DEPTH_TEST):
                print('--> disable GL_DEPTH_TEST')
                glDisable(GL_DEPTH_TEST)
            else:
                print('--> enable GL_DEPTH_TEST')
                glEnable(GL_DEPTH_TEST)

        elif event.key == pygame.K_w:
            print('dinosaur Forwards')
            self.moveForwardFlagger = not self.moveForwardFlagger

        elif event.key == pygame.K_r:
            # Toggle the rotation flag when 'r' is pressed
            self.rotateFlagger = not self.rotateFlagger


    def move_dinosaur_forward(self):
        if self.moveForwardFlagger:
            # Extract the current position of the dinosaur
            current_position = self.dinosaur.M[:3, 3]

            # Extract the Z-axis of the dinosaur (local forward direction)
            dinosaur_direction = self.dinosaur.M[:3, 2]

            # Calculate the new position by moving in the local Z-axis direction
            new_position = current_position + dinosaur_direction * self.dinosaur_speed

            # Update the translation part of the dinosaur's transformation matrix
            self.dinosaur.M[:3, 3] = new_position

            # Trigger a redraw or update the scene to reflect the changes
            # self.draw() or any relevant function to update the scene

    def rotate_dinosaur(self):
        # Continuously rotate until r is pressed again
        if self.rotateFlagger:
            # Get the current position of the dinosaur
            current_position = self.dinosaur.M[:3, 3]

            # Calculate the local origin of the dinosaur
            local_origin = current_position - self.dinosaur.M[:3, 2] * 0.5  # Assuming the local forward direction is the Z-axis

            # Translate the dinosaur to its local origin
            translation_to_origin = translationMatrix(-local_origin)
            self.dinosaur.M = np.matmul(translation_to_origin, self.dinosaur.M)

            # Calculate sine and cosine of rotation angle (convert degrees to radians)
            angle_radians = radians(self.rotation_angle)
            sin_angle = sin(angle_radians)
            cos_angle = cos(angle_radians)

            # Create rotation matrix around dinosaur's local Y-axis
            rotation_matrix = np.array([
                [cos_angle, 0, sin_angle, 0],
                [0, 1, 0, 0],
                [-sin_angle, 0, cos_angle, 0],
                [0, 0, 0, 1]
            ])

            # Apply the rotation to the dinosaur's local transformation matrix
            self.dinosaur.M = np.matmul(rotation_matrix, self.dinosaur.M)

            # Translate the dinosaur back to its original position
            translation_back = translationMatrix(local_origin)
            self.dinosaur.M = np.matmul(translation_back, self.dinosaur.M)


if __name__ == '__main__':
    # Initialize the scene
    scene = ExeterScene()

    # Run the scene
    scene.run()

