<script>
    import App from "./App.svelte";

    export const actions = {
        login: async (event) => {
            // TODO log the user in
        },
        register: async (event) => {
            // TODO register the user
        }
    }
    let filename = "";
    let arr = []

    // Function to handle file input change
    function handleFileChange(event) {
        const file = event.target.files[0];
        if (file) {
            filename = file.name;
            arr = [...arr,filename]
            console.log(arr)
        }
    }
</script>

<main>
    <form method="POST" action="?/login">
        <label>
            <input name="email" type="file" on:change={handleFileChange} />
            {#if filename}
                {#each arr as file}
                    <p> {file} </p>
                {/each}
            {/if}
        </label>
    </form>
</main>
