SCRIPT_TEMPLATE_COMMENTS = """// Hatch Template Object
// Description: A template object for examples of default Hatch entity methods.

// This object is a template that includes each of the
// default entity methods in every Hatch object.
// If necessary, please utilize this when making new objects
// or as a reference.

// Called when the object is loaded into the scene.
// It would be ideal to use this for loading resources (sprites, sounds, models, etc.)
// as well as managing/resetting class-tied static variables.
event {classname}_Load() {{
}}

// Called once per frame when the object is loaded in the scene.
// Useful for managing variables that belong to the class rather than a specific entity.
event {classname}_GlobalUpdate() {{
}}

// Similar to GlobalUpdate, but only runs when the engine is not using fixed time steps.
// If the engine is not using fixed time steps, this will run at the engine's target FPS (default 60).
// event {classname}_GlobalFixedUpdate() {{
// }}

class {classname} {{
    // Static variable
    // Tied to the class and kept between scenes.
    // This particular variable would be "Template.Example".
    // It is useful to have variables for sprites, sounds, models, etc.,
    // then set the variables to Resource load calls in _Load.
    static Example = 0;
    
    // Initializer (Constructor)
    // This runs before Create when an entity is created.
    // The name of the Initializer matches the class name.
    // It is ideal to use this to set default variable values
    // and check properties.
    // Also, making an entity with "new [Object Name]" will just use this method.
    // If that's the case, you can make the initializer have args.
    // However, if the Initializer has an argument(s), you will receive an error
    // when using Instance.Create for that object type.
    {classname}() {{ 
    }}
    
    // Called when the entity is officially added to the scene.
    // Takes an optional arg. For consistency's sake, pass an arg to avoid errors across Gateway.
    Create(data) {{
    }}
    
    // Runs after "Create" of all entities.
    // Ideal for logic that may depend on other entities being fully initialized.
    PostCreate() {{
    }}
    
    // Runs before "Update" of all entities.
    // Useful for resetting flags or other pre-physics logic.
    UpdateEarly() {{
    }}
    
    // Similar to UpdateEarly; see note on GlobalUpdate
    // FixedUpdateEarly() {{
    // }}
    
    // The primary logic loop for movement or management.
    Update() {{
    }}
    
    // Similar to Update; see note on GlobalUpdate
    // FixedUpdate() {{
    // }}
    
    // Runs after "Update" of all entities.
    // Ideal for camera following or resolving collisions.
    UpdateLate() {{
    }}
    
    // Similar to UpdateLate; see note on GlobalUpdate
    // FixedUpdateLate() {{
    // }}
    
    // Runs before "Render" of all entities.
    // Useful for background elements or setting up complex rendering.
    RenderEarly() {{
    }}
    
    // Main rendering event.
    // If not defined, Hatch will use standard sprite drawing,
    // which will draw the entity using its current sprite, animation, and frame
    // at its current X and Y values.
    // However, Gateway purposefully disables this behavior.
    // If you would like to turn it back on, see "init".
    Render() {{
    }}
    
    // Runs after "Render" of all entities.
    // Useful for foreground elements, overlays, or debug info.
    RenderLate() {{
    }}
    
    // Called when the entity's sprite animation completes its last frame.
    OnAnimationFinish() {{
    }}
    
    // Called when the scene is first loaded.
    OnSceneLoad() {{
    }}
    
    // Called if the current scene is reloaded/restarted.
    OnSceneRestart() {{
    }}
    
    // Distructor
    // Called when the entity is removed.
    // Ideal for cleaning up manually allocated resources or stopping sounds.
    Dispose() {{
    }}
}}
"""

SCRIPT_TEMPLATE = """event {classname}_Load() {{
}}

event {classname}_GlobalUpdate() {{
}}

// event {classname}_GlobalFixedUpdate() {{
// }}

class {classname} {{
    static Example = 0;

    {classname}() {{ 
    }}
    
    Create(data) {{
    }}
    
    PostCreate() {{
    }}

    UpdateEarly() {{
    }}
    
    // FixedUpdateEarly() {{
    // }}
    
    Update() {{
    }}
    
    // FixedUpdate() {{
    // }}
    
    UpdateLate() {{
    }}
    
    // FixedUpdateLate() {{
    // }}
    
    RenderEarly() {{
    }}
    
    Render() {{
    }}

    RenderLate() {{
    }}

    OnAnimationFinish() {{
    }}

    OnSceneLoad() {{
    }}

    OnSceneRestart() {{
    }}
    
    Dispose() {{
    }}
}}
"""

GAME_CONFIG_TEMPLATE = """<gameconfig>
    <gameTitle>{game_title}</gameTitle>
    <shortTitle>{short_title}</shortTitle>
    <developer>{developer}</developer>
    <description>Cool description.</description>
    <version>
        <major>1</major>
        <minor>0</minor>
    </version>
 
    <!-- <startscene>Scenes/Start.tmx</startscene> -->
 
    <display>
        <width>424</width>
        <height>240</height>
    </display>
 
    <audio volume="50">
        <music volume="100"></music>
        <sound volume="50"></sound>
    </audio>
 
    <keys>
        <fullscreen>F4</fullscreen>
    </keys>
</gameconfig>
"""

INIT_TEMPLATE = """class Init
{
	GameStart()
	{
		print("Hello world!");
	}
}
"""